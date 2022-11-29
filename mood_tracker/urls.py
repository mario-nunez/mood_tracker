"""mood_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include


handler500 = 'apps.core.views.error_500'
handler500 = 'apps.core.views.error_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.mood_tracker.urls')),
    path('', include('apps.diary.urls')),
    path('', include('apps.self_improvement.urls')),
    path('', include('apps.core.urls')),
    path('', include('django.contrib.auth.urls')),

]
