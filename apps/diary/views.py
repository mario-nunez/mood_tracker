from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Diary
from .serializers import DiarySerializer

# Create your views here.

class DiaryList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'diary/diary.html'

    def get(self, request):
        diary_entries = Diary.objects.all()
        serializer = DiarySerializer(diary_entries, many=True)

        # Get data group by days

        data = {
            'diary_entries': serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        pass