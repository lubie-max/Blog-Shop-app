from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.

def blog(request):
    blogposts= Post.objects.all()
    context= {
        "blogposts":blogposts
    }
    return render(request, 'blog.html', context)

def blogpost(request, slug):
    blogs= Post.objects.filter(slug=slug).first()
    cat= Post.objects.all()
    

    print(cat)

    context= {
        'slug':slug, 'blogs':blogs
    }
    return render( request, 'blogpost.html',context)

def blogger(request):
    return render( request, 'blogger.html')

def aboutblog(request):
    return  render( request, 'aboutblog.html')



