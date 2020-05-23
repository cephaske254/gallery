from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.get_all()

    return render(request,'index.html',{
        'title':'Home | FL Gallery',
        'posts': posts
    })
