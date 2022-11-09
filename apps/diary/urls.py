from django.urls import path

from . import views


urlpatterns = [
    path('diary/', views.DiaryList.as_view(), name='diary'),
]
