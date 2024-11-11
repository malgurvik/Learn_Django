from django.contrib import admin
from django.urls import path, include

from .views import index, heads_or_tails, dice, random_number

urlpatterns = [
    path('', index, name='index'),
    path('heads_or_tails/', heads_or_tails, name='heads_or_tails'),
    path('dice/', dice, name='dice'),
    path('random_number/', random_number, name='random_number'),
]
