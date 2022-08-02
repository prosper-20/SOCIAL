from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment} - {self.author}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name="user", related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_day = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(default="uploads/default.jpg", upload_to="uploads/profile_pictures", blank=True)

    def __str__(self):
        return self.user.username


    
    


