from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blof Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
{
        'author': 'CollyMS',
        'title': 'BloG Post 13',
        'content': 'Second post content',
        'date_posted': 'july 17, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
