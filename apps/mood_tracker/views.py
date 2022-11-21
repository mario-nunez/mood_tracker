from django.db.models import Avg, Count
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
        user_profile = UserProfile.objects.get(user_id=request.user.id)

        # Home table - Get user data grouped by days
        user_moods = Mood.objects.filter(user_profile_id=user_profile.id)\
                                 .order_by('-day_date')
        moods_by_day = user_moods.values('day_date', 'day_week')\
                                 .annotate(total_moods=Count('emotion'),
                                           avg_rate=Avg('reaction_rate'))
        serializer = MoodsDaySerializer(moods_by_day, many=True)

        # Avg rate card - Get total average reaction rate of a user

        # Achievements card - Get total achievements accomplished by a user
        achievements = Achievement.objects.all()

        data = {
            'moods': serializer.data,
            'user_avg_rate': 2.7,
            'max_rate': MAX_REACTION_RATE,
            'user_achievements': 16,
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
