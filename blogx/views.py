from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
# Create your views here.

class AuthorHomeView(ListView):
    """main page"""
    template_name = 'blogx/author_home.html'
    model = Article

class AuthorCreateView(CreateView):
    """main page"""
    template_name = 'blogx/author_home.html'
    model = Article

class AuthorArticleView(UpdateView):
    """main page"""
    template_name = 'blogx/author_article.html'
    model = Article


class HomeView(ListView):
    """main page"""
    template_name = 'blogx/home.html'
    model = Article

class ArticleView(DetailView):
    """main page"""
    template_name = 'blogx/article.html'
    model = Article
