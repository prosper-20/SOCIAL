from django.contrib import admin
from .models import Post, Comment, UserProfile

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["created_on", "author"]

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment", "author", "post"]


admin.site.register(Comment, CommentAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "birthday", "location"]

