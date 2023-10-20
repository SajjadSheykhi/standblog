from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit/', views.edit_user, name='edit')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
