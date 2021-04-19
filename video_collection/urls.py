from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')  # empty string in path('',) means home page
]
