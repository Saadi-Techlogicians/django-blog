from django.shortcuts import render
from django.http import HttpResponse

Post = [
    {
        'author':'Saadi mohammed',
        'title':'Blog Post 1',
        'content':' First post content',
        'date_posted': 'January 3, 2021'
    },
    {
        'author':'Neaz mohammed',
        'title':'Blog Post 2',
        'content':' Second post content',
        'date_posted': 'January 4, 2021'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': Post
    }
    return render(request, "blog/home.html", context)

def about(request):
    title = 'About'
    return render(request, "blog/about.html", {'title':title})
