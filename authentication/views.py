from django.shortcuts import render

def login_register(request):
    return render(request, 'auth/login-register.html')

def logout_user(request):
    pass