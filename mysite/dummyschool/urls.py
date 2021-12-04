from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index.html'),
    path('index.html', views.index, name='index.html'),
    path('faculty.html', views.faculty, name='faculty.html'),
    path('contact.html', views.contact, name='contact.html'),
]