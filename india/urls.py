from django.urls import path
from india.views import *
app_name='india'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('virat/',virat,name='virat'),
]