from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
    context = {
        'title':'Home',
        'heading':'selamat Datang',
    }
    return HttpResponse("Ini home")

