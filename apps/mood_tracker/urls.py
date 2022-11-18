from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeList.as_view(), name="home"),
    path('moods/', views.MoodList.as_view(), name="moods"),
    path('charts/', views.MoodCharts.as_view(), name="charts"),
]
