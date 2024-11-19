from django.urls import path

from .views import index, add_new_author

urlpatterns = [
    path('', index, name='index'),
    path('add_new_author/', add_new_author, name='add_new_author'),

]
