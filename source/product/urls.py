from django.contrib import admin
from django.urls import path
from .views import index, register

app_name = 'product'
urlpatterns = [
    path('', index, name='index'),
    path('/register/', register, name='register'),
]
