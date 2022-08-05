from django.contrib import admin
from django.urls import path, include
from authentication import views




urlpatterns = [
    path('login/', views.login_register, name='login_register'),
    path('logout/', views.logout_user, name='logout'),
]
