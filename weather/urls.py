from django.urls import path, include
from weather.views import *
urlpatterns = [
    path('',index,name='index'),
]