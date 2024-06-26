from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Post,Category,Like,Comment,Bookmark
from .forms import ContactForm, commentForm,SubscribeForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def HomePage(request):
    stories = Post.objects.all().order_by('?')[:5]
    stories_ordered_by_likes = Post.objects.all().order_by('-likes')[:3]

    filterTech= Post.objects.filter(Q(category__name ='Tech')).order_by('?')[:3]
    filterBusiness= Post.objects.filter(Q(category__name ='Business')).order_by('?')[:3]
    filterHealth= Post.objects.filter(Q(category__name ='Health')).order_by('?')[:3]


    context={
        'stories': stories,
        'filterTech': filterTech,
        'filterBusiness': filterBusiness,
        'filterHealth': filterHealth,
        'stories_ordered_by_likes':stories_ordered_by_likes,
        
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def PostDetails(request,slug):
    story = get_object_or_404(Post, slug=slug)
    reviews = Comment.objects.filter(post=story)
    likeCount= Like.objects.filter(post=story).count()
    stories = Post.objects.filter(Q(category__name=story.category)).exclude(slug=story.slug).order_by('?')
    if request.method == 'POST':
            form = commentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user  
                comment.post = story
                story.comments +=1
                story.save()
                comment.save()
                messages.success(request, 'Your Review Added successfully!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER') )
    else:
        form = commentForm()
    context={
        'story': story,
        'stories': stories,
        'likeCount': likeCount,
        'form': form,
        'reviews':reviews
    }
    return render(request, 'postDetails.html', context)

def AllStory(request):
    stories = Post.objects.all()

    # searching the  post 
    query = request.GET.get('search')
    if query:
        stories = Post.objects.filter(Q(title__contains=query) )
    else:
        stories = Post.objects.all().order_by('-id')


    # pagination
    items_per_page = 8
    paginator = Paginator(stories, items_per_page)
    page = request.GET.get('page')
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    context={
    'stories': stories
    }
    return render(request, 'AllStories.html', context)

def TechFilter(request):
    filterTech= Post.objects.filter(Q(category__name ='Tech')).order_by('?')
    context={
        'filterTech':filterTech
    }
    return render(request, 'TechFilter.html', context)

# MVT = MODEL VIEW Template 
    
def BusinessFilter(request):
    filterBusiness= Post.objects.filter(Q(category__name ='Business')).order_by('?')
    context={
        'filterBusiness':filterBusiness
    }
    return render(request, 'BusinessFilter.html', context)


def HealthFilter(request):
    filterHealth= Post.objects.filter(Q(category__name ='Health')).order_by('?')
    context={
        'filterHealth':filterHealth
    }
    return render(request, 'HealthFilter.html', context)

def CategoryFilter(request,category_name):
    category = get_object_or_404(Category, name=category_name)
    data = Post.objects.filter(Q(category__name=category))
    # pagination
    items_per_page = 8
    paginator = Paginator(data, items_per_page)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context={
        'data':data,
        "category_name":category_name
    }
    return render(request, 'allCategoryContent.html', context)


@login_required(login_url='login')
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    if Like.objects.filter(post=post, user=request.user).exists():
        Like.objects.filter(post=post, user=request.user).delete()
        post.likes -=1
        post.isLike = False
        messages.success(request, 'Your dislike successfully!')
        post.save()
    else:
        Like.objects.create(post=post,user=request.user)
        post.likes +=1
        post.isLike = True
        messages.success(request, 'Your Like successfully!')
        post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

@login_required(login_url='login')
def add_bookmark(request, pk=None):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        Bookmark.objects.get_or_create(user=request.user, post=post)
        post.bookmarks +=1
        messages.success(request, 'Your Bookmark Added successfully!')
        post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

def remove_bookmark(request, pk=None):
    data = get_object_or_404(Bookmark, pk=pk)
    data.post.bookmarks -=1
    data.save()

    data.delete() 
    messages.success(request, 'Your bookmark remove successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

@login_required(login_url='login')
def bookmarksCollection(request):
    bookmarks=Bookmark.objects.filter(user=request.user)
    context={
        'bookmarks': bookmarks
    }
    return render(request,'bookmarks.html',context)


def about(request):
    return render(request,'about.html')


def LikeView(request,pk=None):
    post = get_object_or_404(Post,pk=pk)
    likeView = get_object_or_404(Like,post=post)
    context={
        'likeView':likeView,
    }
    return render(request,'Stories.html',context)





def ContactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Contact submit successfully!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER') )
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form': form})

from django.core.mail import send_mail
from django.conf import settings
def SubscriptionPage(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            subject = 'Subscription Successful'
            message = f'Thank you {subscription.name} for subscribing to dev.io site!'
            recipient_list = [subscription.email]
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            messages.success(request, 'You are subscribed successfully!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = SubscribeForm()
    return render(request, 'subscribe.html', {'form': form})