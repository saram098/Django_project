from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

posts = [
    {
        'author': 'Saram',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 17, 2023'
    },
    {
        'author': 'Anas',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 18, 2023'
    },
    {
        'author': 'Zohaib',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'March 19, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

