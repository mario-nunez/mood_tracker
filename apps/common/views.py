from django.shortcuts import redirect
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class SignUp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/sign_up.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        pass