from django import urls
from django.urls import path
from django.conf import settings
from . import views





urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]