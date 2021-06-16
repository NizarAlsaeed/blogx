from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

class AuthorCreateView(CreateView):
    """main page"""
    template_name = 'blogx/author_create.html'
    model = Article
    fields = ['title', 'author', 'content']

class AuthorUpdateView(UpdateView):
    """main page"""
    template_name = 'blogx/author_update.html'
    model = Article
    fields = ['title', 'author', 'content']

class AuthorDeleteView(DeleteView):
    """main page"""
    template_name = 'blogx/author_delete.html'
    model = Article
    fields = ['title', 'author', 'content']
    success_url = reverse_lazy('home')

class HomeView(ListView):
    """main page"""
    template_name = 'blogx/home.html'
    model = Article

class ArticleView(DetailView):
    """main page"""
    template_name = 'blogx/article.html'
    model = Article
