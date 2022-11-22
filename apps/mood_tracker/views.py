from django.db.models import Avg, Count
from django.db.models.functions import Round
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .constants import MAX_REACTION_RATE
from .models import Mood
from .serializers import MoodSerializer, MoodsDaySerializer
from ..common.decorators import authentication_required
from ..common.models import Achievement, UserProfile


# Create your views here.

class HomeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mood_tracker/home.html'

    @authentication_required
    def get(self, request):
        # Filter by user information
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        user_moods = Mood.objects.filter(user_profile_id=user_profile.id)\
                                 .order_by('-day_date')

        # Home table - Get user data grouped by days
        moods_by_day = user_moods.values('day_date', 'day_week')\
                                 .annotate(total_moods=Count('emotion'),
                                           day_avg_rate=Avg('reaction_rate'))
        serializer = MoodsDaySerializer(moods_by_day, many=True)

        # Avg rate card - Get total average reaction rate of a user
        total_avg_rate = user_moods.aggregate(
            total_avg_rate=Round(Avg('reaction_rate'), precision=1)
        )['total_avg_rate']

        # Achievements card - Get total achievements accomplished by a user
        achievements = Achievement.objects.all()
        user_achievements = user_profile.achievements.aggregate(
            total_achievements=Count('title')
        )

        # Days registered
        days_registered = moods_by_day.aggregate(total_days=Count('day_date'))

        data = {
            'day_moods': serializer.data,
            'days_registered': days_registered['total_days'],
            'user_avg_rate': total_avg_rate,
            'max_rate': MAX_REACTION_RATE,
            'user_achievements': user_achievements['total_achievements'],
            'total_achievements': achievements.count()
        }

        return Response(data, status=status.HTTP_200_OK)


class MoodList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mood_tracker/moods.html'

    @authentication_required
    def get(self, request):
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        user_moods = Mood.objects.filter(user_profile_id=user_profile.id)
        serializer = MoodSerializer(user_moods, many=True)

        data = {
            'moods': serializer.data
            }
        return Response(data, status=status.HTTP_200_OK)

    @authentication_required
    def post(self, request):
        pass


class MoodCharts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mood_tracker/charts.html'

    @authentication_required
    def get(self, request):
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        user_moods = Mood.objects.filter(user_profile_id=user_profile.id)
        serializer = MoodSerializer(user_moods, many=True)

        data = {
            'moods': serializer.data
            }
        return Response(data, status=status.HTTP_200_OK)
