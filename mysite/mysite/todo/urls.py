from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.todo, name='todo.html'),
    path('delete/<str:pk>', views.delete, name='delete')
]