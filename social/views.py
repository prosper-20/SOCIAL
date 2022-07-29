import imp
from re import S
from django.shortcuts import render
from django.views import View
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()



        context = {
            'posts': posts,
            'form': form
        }
        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'posts': posts,
            'form': form
        }
        return render(request, 'social/post_list.html', context)



class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        context = {
            "post": post,
            "form": form,
        }
        return render(request, 'social/post_detail.html', context)
        

class PostEditView(UpdateView):
    model = Post
    fields = ["body"]
    template_name = "social/post_edit.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy('post-detail', kwargs={"pk": pk})

class PostDeldtdView(DeleteView):
    model = Post
    template_name = "social/post_delete.html"
    success_url = reverse_lazy("post-list")

            

