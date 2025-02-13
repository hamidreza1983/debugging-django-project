from django.urls import path
from .views import *

app_name = "blogs"

urlpatterns = [
    path('', BlogView.as_view(), name="blogs"),
    path('detail/<int:pk>', BlogDetailsView.as_view(), name="blogs_details"),
    path('category/<str:category>', BlogView.as_view(), name="blogs_category"),
    path('tag/<str:tag>', BlogView.as_view(), name="blogs_tag"),
]