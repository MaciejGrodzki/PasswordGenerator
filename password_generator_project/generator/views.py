from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def select(request):
    return render(request, 'select.html')

def password(request):
    return render(request, 'password.html' )