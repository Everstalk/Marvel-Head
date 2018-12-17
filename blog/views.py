from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader 

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def post_list(request):
    latest_post_list = Post.objects.order_by('-published_date')[:5]
    context = {
        'latest_post_list': latest_post_list
    }
    return render(request, 'blog/post_list.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})

def results(request, post_id):
    response = "You're looking at the results of Post %s."
    return HttpResponse(response % post_id)

def new_post(request):
    form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})

