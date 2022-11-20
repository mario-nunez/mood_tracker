from django.urls import path

from . import views


urlpatterns = [
    path('sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('about/', views.About.as_view(), name='about'),
    path('achievements/',
         views.UserAchievements.as_view(),
         name='achievements'),
    path('settings/', views.UserSettings.as_view(), name='settings'),
    path('dashboard/', views.AdminDashboard.as_view(), name='dashboard'),

]
