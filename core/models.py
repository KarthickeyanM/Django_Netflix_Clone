from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

AGE_CHOICES = (
    ('All','All'),
    ('Kids','Kids')
)

MOVIE_CHOICES = (
    ('seasonal','seasonal'),
    ('single','single'),
)


class CustomUser(AbstractUser):
    profile = models.ManyToManyField('Profile')

class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)
    def __str__(self):
        return self.name +" "+ self.age_limit
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10,choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers/')
    age_limit = models.CharField(max_length=10,choices=AGE_CHOICES)

    def __str__(self): 
        return self.title
    
class Video(models.Model):
    title: str = models.CharField(max_length=255,blank=True,null=True )
    file = models.FileField(upload_to='movies/')

    def __str__(self):
        return self.title