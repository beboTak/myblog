
from django.urls import path
from .views import home, article_create, register, article_detail

urlpatterns = [
    path('', home, name='home'),
    path('article/new/', article_create, name='article_create'),
    path('register/', register, name='register'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
]