from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Post
from .serializers import PostSerializer

class PostsList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostsDetail(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
