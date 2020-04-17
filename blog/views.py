from django.shortcuts import render
from .models import Post
from django.views import generic
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


    




