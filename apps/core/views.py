from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .decorators import (authentication_not_required, authentication_required,
                         admin_only)
from .forms import CreateUserForm, UserProfileForm
from .models import UserProfile, Achievement
from .serializers import AchievementSerializer


class SignUp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/sign_up.html'

    @authentication_not_required
    def get(self, request):
        form = CreateUserForm()
        context = {'form': form}
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        form = CreateUserForm(request.data)

        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile.objects.create(user=user)
            messages.success(request, "Registration successful.")
            return redirect('login')

        context = {'form': form}

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
    template_name = 'core/about.html'

    @admin_only
    @authentication_required
    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class UserSettings(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'core/settings.html'

    @authentication_required
    def get(self, request):
        user_info = request.user.userprofile
        form = UserProfileForm(instance=user_info)
        context = {'form': form}
        return Response(context, status=status.HTTP_200_OK)

    @authentication_required
    def post(self, request):
        pass


class UserAchievements(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'core/achievements.html'

    @authentication_required
    def get(self, request):
        user_achievements = UserProfile.objects\
            .filter(user_id=request.user.id)\
            .values_list('achievements', flat=True)
        achievements = Achievement.objects.all()

        print(user_achievements)
        print(achievements)

        serializer = AchievementSerializer(achievements, many=True)

        data = {
            'achievements': serializer.data,
            'user_achievements': user_achievements
        }

        return Response(data, status=status.HTTP_200_OK)

    @admin_only
    @authentication_required
    def post(self, request):
        return Response(status=status.HTTP_200_OK)


class AdminDashboard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'core/admin_dashboard.html'

    @admin_only
    @authentication_required
    def get(self, request):
        return Response(status=status.HTTP_200_OK)


# Redirecto to custom error pages
def error_404(request):
    return render(request, 'core/404.html')


def error_500(request):
    return render(request, 'core/500.html')
