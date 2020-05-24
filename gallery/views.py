from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpRequest, request
from django.contrib import messages
# Create your views here.

def index(request):
    posts = Post.get_all()

    return render(request,'index.html',{
        'title':'Home | FL Gallery',
        'posts': posts
    })

def copy_link(request, id):
    host = HttpRequest.get_host(request)
    link = Post.copy_link(host,id)
    messages.add_message(request,messages.SUCCESS, f'Copied <span class="alert-link">{link}</span> to clipboard!',extra_tags='alert-success',fail_silently=True,)
    return redirect('../')
