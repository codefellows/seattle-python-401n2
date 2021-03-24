from django.urls import path

from .views import BlogList, BlogDetail

urlpatterns = [
    path("<int:pk>/", BlogDetail.as_view()),
    path("", BlogList.as_view()),
]