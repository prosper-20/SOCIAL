from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["created_on", "author"]

admin.site.register(Post, PostAdmin)
