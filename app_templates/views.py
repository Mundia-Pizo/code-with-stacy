from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snippet


class CodeTemplateListView(ListView):
    model = Snippet
    template_name = 'app_templates/templates.html'
    

class CodeDetailView(DetailView):
    model =Snippet
    template_name='app_templates/template_detail.html'