from django.urls import path 
from .views import Index


urlpaterns = [
    path("", Index.as_view(), name="home")
]