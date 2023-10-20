from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/article')
    slug = models.SlugField(blank=True, unique=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    class Meta:
        ordering = ('-create', '-update')
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name="replies")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class Message(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
