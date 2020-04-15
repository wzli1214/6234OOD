from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import Http404

from Insta.models import Post

# Create your views here.

class HelloDjango(TemplateView):
    template_name = 'home.html'

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    
# class PostView(ListView):
#     model = Post
#     template_name = 'posts.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = "make_post.html"
    fields = '__all__' 


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title']
    template_name = 'post_edit.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

def blog_detail_view(request, primary_key):
    try:
        post = Post.objects.get(pk=primary_key)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')

    return render(request, 'post_detail.html', context={'post':post})