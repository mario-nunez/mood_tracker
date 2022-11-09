from django.urls import path

from . import views


urlpatterns = [
    path('lessons/', views.LessonList.as_view(), name="lessons"),
]
