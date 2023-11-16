from django.urls import path
from nz.views import *
app_name='nz'
urlpatterns=[
    path('kane/',kane,name='kane'),
    path('phillips/',phillips,name='phillips'),
]