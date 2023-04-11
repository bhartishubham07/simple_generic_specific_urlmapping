from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

def forgetpass(request):
    return render(request, 'forgetpass.html')

def otp(request):
    return render(request, 'otp.html')

def home(request):
    return render(request, 'home.html')

def add(request):
    return render(request, 'add.html')

def get(request):
    return render(request, 'get.html')

def delete(request):
    return render(request, 'delete.html')

