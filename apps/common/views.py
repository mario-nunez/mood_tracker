from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CreateUserForm
from .decorators import authentication_not_required, authentication_required

# Create your views here.


class SignUp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/sign_up.html'

    @authentication_not_required
    def get(self, request):

        form = CreateUserForm()
        context = { 'form': form }

        return Response(context, status=status.HTTP_200_OK)
    
    def post(self, request):
        form = CreateUserForm(request.data)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('login')

        context = { 'form': form }

        return Response(context, status=status.HTTP_400_BAD_REQUEST)


class LogIn(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/login.html'

    @authentication_not_required
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')


class LogOut(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/login.html'

    @authentication_required
    def get(self, request):
        logout(request)
        return redirect('login')
    

class About(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'common/about.html'

    @authentication_required
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

class UserSettings(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'common/settings.html'

    @authentication_required
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

class UserAchievements(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'common/achievements.html'

    @authentication_required
    def get(self, request):
        return Response(status=status.HTTP_200_OK)