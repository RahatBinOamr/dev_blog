from django.urls import path
from .views import createPost,postCollection,removePost,updatePost
urlpatterns = [
    path('create/',createPost,name='create'),
    path('postManagement/',postCollection,name='postManagement'),
    path('update/<pk>',updatePost,name='update'),
    path('remove/<pk>',removePost,name='remove'),
]
