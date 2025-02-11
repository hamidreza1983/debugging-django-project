from django.urls import path
from .views import ServicesView

app_name = "services"

urlpatterns = [
    path("", ServicesView.as_view(), name="services"),
]