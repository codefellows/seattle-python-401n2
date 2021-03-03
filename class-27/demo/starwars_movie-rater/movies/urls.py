from movies.models import Movie
from django.urls import path, include
from .views import MovieDetailView, MovieListView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]