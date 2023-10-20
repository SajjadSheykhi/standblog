from django.shortcuts import render
from blog.models import Article


# Create your views here.

def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all()[:3]
    context = {'articles': articles, 'recent_articles': recent_articles}
    return render(request, 'home/index.html', context)



def sidebar(request):
    context = {"name": 'sajjad'}
    return render(request, 'includes/sidebar.html', context)