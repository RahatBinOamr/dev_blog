
from typing import Any
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import re

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=250)
  parent_category = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True,related_name='child')
  image = models.ImageField(upload_to='category/',default='category/default.png')

  def __str__(self) :
    return self.name

class Status(models.Model):
  name = models.CharField(max_length=250)

  def __str__(self):
    return self.name
  

class SubCategory(models.Model):
  name = models.CharField(max_length=250)
  category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)

  def __str__(self):
    return self.name



class Post(models.Model):
  title = models.CharField(max_length=300)
  image = models.ImageField(upload_to='Post/',default='default.png')
  description = RichTextField()
  sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True,null=True)
  category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
  status = models.ForeignKey(Status,on_delete=models.CASCADE,blank=True,null=True)
  slug =AutoSlugField(populate_from='title',unique=True)
  likes = models.IntegerField(default=0,null=True,blank=True)
  comments = models.IntegerField(default=0,null=True,blank=True)
  bookmarks = models.IntegerField(default=0,null=True,blank=True)
  isLike = models.BooleanField(default=False, null=True,blank=True)
  isBookmark = models.BooleanField(default=False, null=True,blank=True)
  video_url = models.URLField(null=True, blank=True)  
  tutorial_url = models.URLField(null=True, blank=True)  

  def has_video(self):
        return bool(self.video_url)
  
  def has_tutorial(self):
        return bool(self.tutorial_url)

  def get_youtube_video_id(self):
  
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )
        matches = re.match(youtube_regex, self.video_url)
        if matches:
            return matches.group(6)
        return None
  
  def get_youtube_tutorial_id(self):
  
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )
        matches = re.match(youtube_regex, self.tutorial_url)
        if matches:
            return matches.group(6)
        return None
  


  def __str__(self):
    return self.title
  
  def get_like_count(self):
        return self.like_set.count()
  
  def get_comments_count(self):
        return self.comment_set.count()
        
  def get_bookmarks_count(self):
        return self.bookmark_set.count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      return self.post.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    comment = models.TextField()

    def __str__(self):
      return self.comment
    
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
      return self.post.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Subscribe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name