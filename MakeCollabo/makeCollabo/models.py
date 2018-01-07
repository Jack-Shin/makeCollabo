from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey('auth.user')
  title = models.CharField(max_length=256)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title

class Star(models.Model):
  post = models.ForeignKey('makeCollabo.Post', related_name='hearts')
  who = models.ForeignKey('auth.user')

class Comment(models.Model):
  post = models.ForeignKey('makeCollabo.Post', related_name='comments')
  #author = models.CharField(max_length=128)
  author = models.ForeignKey('auth.user')
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)