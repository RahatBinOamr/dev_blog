from django.contrib import admin
from .models import Category,Post,SubCategory,Status,Like,Comment,Bookmark,Contact,Subscribe
# Register your models here.
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Bookmark)
admin.site.register(Contact)
admin.site.register(Subscribe)