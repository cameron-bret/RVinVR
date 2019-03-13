from django.shortcuts import render
from .models import Post

def index(request):
  queryset = Post.objects.filter(featured=True)
  context = {
    'object_list': queryset
  }
  return render(request, 'index.html', context)

def blog(request):
  return render(request, 'blog.html', {})

def post(request):
  return render(request, 'post.html', {})