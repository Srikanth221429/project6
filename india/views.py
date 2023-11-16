from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return HttpResponse('<h1>Captain of india</h1>')
def virat(request):
    return HttpResponse('<h1>Done a wonderful innings</h1>')