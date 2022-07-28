from django.urls import path

from social.models import Post
from .views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail")
]