from django.urls import path
from .views import *

app_name = 'api_service'

urlpatterns = [
    path('services',api_services,name='services'),
]