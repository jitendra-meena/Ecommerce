from django.contrib import admin
from django.urls import path
from core.views import *
urlpatterns = [
    path('user_data',user_data,name='user_data'),
]


