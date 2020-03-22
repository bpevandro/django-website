"""Defines URL patterns for mywebsite_app."""

from django.urls import path
from . import views

app_name = 'mywebsite_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]