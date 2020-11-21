from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Article


class  ArticleListView(ListView):
    model = Article
    template_name = 'blogs/article_list.html'


