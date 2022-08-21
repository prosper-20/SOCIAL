from django.urls import path

from social.models import Post
from .views import ( 
    PostListView, 
    PostDetailView, 
    PostEditView, 
    PostDeleteView, 
    CommentDeleteView, 
    ProfileView, 
    ProfileEditView, 
    AddFollower, 
    RemoveFollower, 
    DislikeView, 
    AddLike, 
    UserSearch, 
    ListFollowers, 
    AddCommentLike, 
    AddCommentDisLike

)

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/edit/<int:pk>/", PostEditView.as_view(), name="post-edit"),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:post_pk>/comment/delete/<int:pk>/", CommentDeleteView.as_view(), name="comment-delete"),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name="comment-like"),
    path("post/<int:pk>/comment/<int;pk./dislike", AddCommentDisLike.as_view(), name="comment-dislike"),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name="profile-edit"),
    path("profile/<int:pk>", ProfileView.as_view(), name='profile'),
    path("profile/<int:pk>/followers/", ListFollowers.as_view(), name="list-followers"),
    path("profile/<int:pk>/followers/add", AddFollower.as_view(), name="add-follower"),
    path("profile/<int:pk>/followers/remove", RemoveFollower.as_view(), name="remove-follower"),
    path("post/<int:pk>/like", AddLike.as_view(), name="like"),
    path('post/<int:pk>/dislike', DislikeView.as_view(), name="dislike"),
    path('search/', UserSearch.as_view(), name="profile-search"),
    
]