from django.urls import path,include
from .views import ServicesView

app_name = "services"

urlpatterns = [
    path("", ServicesView.as_view(), name="services"),
    path('api/v1/',include('services.api.v1.urls')),
]