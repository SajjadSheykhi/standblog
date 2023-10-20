from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Category, Comment, Message
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm
from django.views.generic import DetailView, ListView, FormView
from django.urls import reverse_lazy


# Create your views here.

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    return render(request, 'blog/article_detail.html', {'article': article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 4)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': objects_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, "blog/articles_list.html", {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 4)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': objects_list})


# def contactus(request):
#     if request.method == 'POST':
#         form = MessageForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home:home')
#     else:
#         form = MessageForm()
#     return render(request, 'blog/contactus.html', {'form': form})


# class ArticleDetailView(DetailView):
#     model = Article


# class ArticleListView(ListView):
#     model = Article
#     template_name = 'blog/articles_list.html'
#     context_object_name = 'articles'
#     paginate_by = 4


class ContactUsView(FormView):
    template_name = 'blog/contactus.html'
    form_class = MessageForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)
        return super().form_valid(form)
