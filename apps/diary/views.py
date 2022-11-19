from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Diary
from .serializers import DiarySerializer
from ..common.decorators import authentication_required

# Create your views here.

class DiaryList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'diary/diary.html'

    @authentication_required
    def get(self, request):
        diary_entries = Diary.objects.all()
        serializer = DiarySerializer(diary_entries, many=True)

        data = {
            'diary_entries': serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)
    
    @authentication_required
    def post(self, request):
        pass