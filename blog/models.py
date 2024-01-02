
from typing import Any
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


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