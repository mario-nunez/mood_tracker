from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MoodTracker
from .serializers import MoodTrackerSerializer

# Create your views here.

class MoodList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'moodtracker/home.html'

    def get(self, request):
        moods = MoodTracker.objects.all()
        serializer = MoodTrackerSerializer(moods, many=True)
        return Response({'moods': serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        pass
