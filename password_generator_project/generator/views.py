from django.shortcuts import render
from random_password import generate_password

def home(request):
    return render(request, 'home.html')

def select(request):
    return render(request, 'select.html')

def password(request):
    length = int(request.POST['length'])
    numbers = request.POST.get('numbers')
    big = request.POST.get('Big')
    special_characters = request.POST.get('special_characters')
    return render(request, 'password.html', {'length':generate_password(length,numbers,big,special_characters)})