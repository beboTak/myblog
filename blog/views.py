from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm, UserRegistrationForm
from django.contrib.auth import login

@login_required
def home(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()

    return render(request, 'home.html', {'form': form, 'articles': articles})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()

    return render(request, 'article_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()

    return render(request, 'article_detail.html', {'article': article, 'form': form, 'comments': comments})
