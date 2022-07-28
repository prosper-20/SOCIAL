from django.urls import path

from social.models import Post
from .views import PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list")
]