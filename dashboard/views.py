from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from .forms import PostForm
from blog.models import Post
# Create your views here.
def createPost(request):
  if request.method == "POST":
      forms = PostForm(request.POST, request.FILES)
      if forms.is_valid():
        forms.save()
        return redirect('postManagement')
  else:
      forms=PostForm()
  context={
      'forms': forms,
  }
  return render(request, 'createPost.html',context)

def postCollection(request):
    posts = Post.objects.all()
    context={
        'posts': posts
    }
    
    return render(request, 'postManagement.html',context)


def updatePost(request,pk=None):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        forms = PostForm(request.POST, request.FILES, instance=post)
        if forms.is_valid():
            forms.save()
            return redirect('postManagement')
    else:
        forms = PostForm(instance=post)

    context={
        'forms':forms
    }
    return render(request, 'updatePost.html',context)

def removePost(request,pk=None):
    item = get_object_or_404(Post, id=pk)
    item.delete()