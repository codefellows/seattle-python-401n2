from django.urls import path
from django.urls.resolvers import URLPattern

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
]