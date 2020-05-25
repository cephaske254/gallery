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

def search_results(request):
    if request.GET and request.GET['search']:
        search_res = Post.search_image(request.GET['search'])
        info = 'Search Results'
        return render(request,'search.html', {'info':info,'posts':search_res})
    else:
        info = 'OOPS! Did you enter any keyword?'
        return render(request,'search.html', {'info':info})


def copy_link(request, id):
    host = HttpRequest.get_host(request)
    link = Post.copy_link(host,id)
    messages.add_message(request,messages.SUCCESS, f'Copied <span class="alert-link">{link}</span> to clipboard!',extra_tags='alert-success',fail_silently=True,)
    if(request.META['HTTP_REFERER']):
        return redirect(request.META['HTTP_REFERER'])
    else :
        return redirect('../')
