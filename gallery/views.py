from django.shortcuts import render, redirect, Http404
from .models import Post,Category
from django.http import HttpRequest, request, HttpResponse
from django.contrib import messages
# Create your views here.

def index(request, category=None, location=None):
    categories = Category.get_all()
    title = 'Home | Fl Gallery'
    posts = Post.get_all()
    if category:
        try: 
            posts = Post.filter_by_category(category)
            title = f'Fl Gallery | Category {category}'
        except:
            raise Http404()
    elif location:
        posts = Post.filter_by_location(location)
        title = f'Fl Gallery | Location {location}'

    return render(request,'index.html',{
        'title':title,
        'posts': posts,
        'categories':categories
    })


def search_results(request):
    title= 'Fl Gallery | Search'
    if request.GET and request.GET['search']:
        search_res = Post.search_image(request.GET['search'])
        info = 'Search Results'
        title= f'Fl Gallery | Search {request.GET["search"]}'
        return render(request,'search.html', {'info':info,'posts':search_res,'title':title})
    else:
        info = 'OOPS! Did you enter any keyword?'
        return render(request,'search.html', {'info':info,'title':title})


def copy_link(request, id):
    host = HttpRequest.get_host(request)
    link = Post.copy_link(host,id)
    return HttpResponse(link)

