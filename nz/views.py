from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kane(request):
    return HttpResponse('<h1><marquee>Captain</marquee><h1>')
def phillips(request):
    return HttpResponse('<h1><marquee>BATSMAN</marquee><h1>')