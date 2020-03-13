"""dogs_project URL"""

from django.urls import path
from . import views

app_name = 'dogs_project'

urlpatterns = [
    path('', views.index, name='index'),

    # Page for adding a new dog
    path('new_dog/', views.new_dog, name='new_dog'),
]