from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lesson
from .serializers import LessonSerializer

# Create your views here.

class LessonList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'self_improvement/lessons.html'

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)

        # Get data group by days

        data = {
            'lessons': serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        pass