from django.contrib import admin
from django.urls import path, include
from authentication import views




urlpatterns = [
    path('signin/', views.sign_in, name='sign_in'),
    path('signup/', views.RegisterView.as_view() , name='sign_up'),
    path('logout/', views.logout_user, name='logout'),
]
