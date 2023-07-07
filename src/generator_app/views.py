from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator_app/index.html')


def pwd(request):
    characters = list('abcdefghijklmnopqrstuvwxy')

    if request.GET.get('upper'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*)(_+=-'))

    length = int(request.GET.get('length', 9))


    password = ''

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator_app/pwd.html', {'password_value': password})


def about(request):
    return render(request, 'generator_app/about.html')
