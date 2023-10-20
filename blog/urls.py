from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path('detail/<slug:slug>', views.article_detail, name="article_detail"),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('list/', views.article_list, name='article_list'),
    path('search/', views.search, name='search'),
    path('contactus/', views.ContactUsView.as_view(), name='contactus'),
]