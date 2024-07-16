from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from .permissions import IsAdminOrReadOnly


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class PostMVS(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()

        return Post.objects.filter(status=2)
