from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.

class Post(models.Model):
  FIND_WHO_CHOICES = (
    ('FE', 'Front End'),
    ('BE', 'Back End'),
    ('BO', 'Both'),
  )
  author = models.ForeignKey('auth.user')
  title = models.CharField(max_length=100)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  find_who = models.CharField(max_length=2, choices=FIND_WHO_CHOICES)
  
class Star(models.Model):
  post = models.ForeignKey('makeCollabo.Post', related_name='hearts')
  who = models.ForeignKey('auth.user')

class Comment(models.Model):
  post = models.ForeignKey('makeCollabo.Post', related_name='comments')
  #author = models.CharField(max_length=128)
  author = models.ForeignKey('auth.user')
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)