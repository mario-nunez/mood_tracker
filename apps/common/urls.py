from django.urls import path

from . import views


urlpatterns = [
    path('sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
]
