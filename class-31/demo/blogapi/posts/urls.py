from django.urls import path
from .views import PostsList, PostsDetail

urlpatterns = [
    path('', PostsList.as_view(), name='posts_list'),
    path('<int:pk>/', PostsDetail.as_view(), name='posts_detail'),
]
