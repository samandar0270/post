from django.urls import path
from .views import *

app_name = 'post_add'
urlpatterns = [
    path('', adding, name='post_add'),
]
