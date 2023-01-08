from django.shortcuts import render
from django.http import HttpResponse
from .processinges import sendDatas

# Create your views here.

def index(request):
    return render(request,'polls.html')

def analisis_data(request):
    name_path = request.resolver_match.url_name
    sendDatas.get_images(name_path)
    return render(request,'Analisis_f.html')
