from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeList.as_view(), name="home"),
    path('moods/', views.MoodList.as_view(), name="moods"),
    path('moods/<str:pk>/', views.MoodDetail.as_view(), name="mood-detail"),
    path('stats/', views.MoodStats.as_view(), name="stats"),
]
