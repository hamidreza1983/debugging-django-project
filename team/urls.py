from django.urls import path
from .views import TeamsView



app_name = "teams"

urlpatterns = [
    path("", TeamsView.as_view(), name="teams"),
]