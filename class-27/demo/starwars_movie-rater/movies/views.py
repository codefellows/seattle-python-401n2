from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie

class MovieListView(ListView):
    template_name = "movie_list.html"
    model = Movie

class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie