from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie
from django.urls import reverse_lazy

class MovieListView(ListView):
    template_name = 'movie-list.html'
    model = Movie

class MovieDetailView(DetailView):
    template_name = 'movie-detail.html'
    model = Movie

class MovieCreateView(CreateView):
    template_name = 'movie-create.html'
    model = Movie
    fields = ['name', 'description', 'owner']

class MovieUpdateView(UpdateView):
    template_name = 'movie-update.html'
    model = Movie
    fields = ['name', 'description', 'owner']

class MovieDeleteView(DeleteView):
    template_name = 'movie-delete.html'
    model = Movie
    success_url = reverse_lazy('movie_list')
