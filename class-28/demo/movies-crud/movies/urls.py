from django.urls import path
from .views import MovieDeleteView, MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('new/', MovieCreateView.as_view(), name='movie_create'),
    path('<int:pk>/edit', MovieUpdateView.as_view(), name='movie_update'),
    path('<int:pk>/delete', MovieDeleteView.as_view(), name='movie_delete'),
]
