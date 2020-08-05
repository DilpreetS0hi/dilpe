from django.shortcuts import render
from .models import Post

#posts=[
#    {
#        'author': 'CoreyMS',
#        'title': 'Blog Post 1',
#        'content': 'First post Content',
#        'date_posted': 'August 27 2020'
#    },
#    {
#        'author': 'Jane Doe',
#        'title': 'Blog Post 2',
#        'content': 'Second post Content',
#        'date_posted': 'August 27 2020'
#    }
#]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
