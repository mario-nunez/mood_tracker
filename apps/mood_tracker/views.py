from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Mood, UserProfile
from .serializers import MoodSerializer, MoodsDaySerializer
from ..common.decorators import authentication_required


# Create your views here.

class HomeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mood_tracker/home.html'

    @authentication_required
    def get(self, request):
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        user_moods = Mood.objects.filter(user_profile_id=user_profile.id)
        serializer = MoodsDaySerializer(user_moods, many=True)

        # Get data group by days

        data = {
            'moods': serializer.data,
            'avg_rate': 6,
            'achievements': 16
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
