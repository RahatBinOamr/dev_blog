from django.urls import path
from blog.views import HomePage,PostDetails,AllStory,TechFilter,BusinessFilter,HealthFilter,CategoryFilter,like_post,add_bookmark, remove_bookmark,bookmarksCollection,about,LikeView,ContactPage,SubscriptionPage

urlpatterns = [
    path('',HomePage,name="home"),
    path('postDetails/<slug>',PostDetails,name="postDetails"),
    path('allStory/',AllStory,name="allStory"),
    path('tech/',TechFilter,name="tech"),
    path('business/',BusinessFilter,name="business"),
    path('health/',HealthFilter,name="health"),
    path('category/<str:category_name>',CategoryFilter,name="category"),
    path('like_post/<pk>', like_post, name='like_post'),
    path('add_bookmark/<pk>', add_bookmark, name='add_bookmark'),
    path('remove_bookmark/<pk>', remove_bookmark, name='remove_bookmark'),
    path('bookmark/', bookmarksCollection, name='bookmark'),
    path('about/', about, name='about'),
    path('contact/', ContactPage, name='contact'),
    path('contact/', ContactPage, name='contact'),
    path('subscribe/', SubscriptionPage, name='subscribe'),
    path('like/<pk>', LikeView, name='like'),
]
