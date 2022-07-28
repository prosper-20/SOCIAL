from django.shortcuts import render
from django.views import View
from .models import Post

# Create your views here.

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')

        context = {
            'posts': posts
        }
        return render(request, 'social/post_list.html', context)
