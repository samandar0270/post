from django.urls import path
from .views import contacting

app_name = 'contact'
urlpatterns = [
    path('', contacting, name='contact'),
]
