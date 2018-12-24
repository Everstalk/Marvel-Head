import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader 
from django.utils import timezone


from .models import Post
from .forms import PostForm


def index(request):
    return render(request,'blog/index.html')

def post_list(request):
    latest_post_list = Post.objects.order_by('-published_date')[:5]
    context = {
        'latest_post_list': latest_post_list
    }
    return render(request, 'blog/post_list.html', context)
"""
def get_post_data(request):
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'blog/post_list.html')
"""
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def results(request, pk):
    response = "You're looking at the results of Post %s."
    return HttpResponse(response % pk)

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/edit_post.html', {'form': form})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

