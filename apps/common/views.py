from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


from .forms import CreateUserForm

# Create your views here.

class SignUp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/sign_up.html'

    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:
            return redirect('home')

        form = CreateUserForm()
        context = { 'form': form }

        return Response(context, status=status.HTTP_200_OK)
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        


class LogIn(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/login.html'

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

    def get(self, request):
        logout(request)
        return redirect('login')
    