from django.urls import path
from .views import PortfolioListView, PortfolioDetailView
app_name = "portfolio"

urlpatterns = [
    path("", PortfolioListView.as_view(), name="portfolio"),
    path("detail/<int:pk>/", PortfolioDetailView.as_view(), name="portfolio-details"),
]