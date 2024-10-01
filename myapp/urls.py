from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage' ),
    path('login',views.loginorsignup, name='login')
]
