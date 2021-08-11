from django.shortcuts import render
from django.views.generic import TemplateView


class MovieView(TemplateView):
    template_name = 'index.html'