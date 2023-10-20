from blog.models import Article, Category


def recent_articles(request):
    recent_article = Article.objects.order_by('-create')
    return {"recent_article": recent_article}


def categories(request):
    categories = Category.objects.all()
    return {"categories": categories}
