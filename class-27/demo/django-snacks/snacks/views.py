from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

class HomePageView(TemplateView):
    template_name = "home.html"

class SnacksListView(ListView):
    template_name = "snacks_list.html"
    model = Snack

class SnacksDetailView(DetailView):
    template_name = "snacks_detail.html"
    model = Snack
