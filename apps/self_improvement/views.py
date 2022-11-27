from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lesson
from .serializers import LessonSerializer
from apps.core.decorators import authentication_required

# Create your views here.


class LessonList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'self_improvement/lessons.html'

    @authentication_required
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)

        data = {
            'lessons': serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        pass
