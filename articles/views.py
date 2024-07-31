from .models import User, Article
from .serializers import UserSerializer, ArticleSerializer, URLSerializer
from .validators import IsAuthor

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import get_resolver
from django.conf import settings
from django.utils.encoding import force_str


class PublicArticleList(generics.ListAPIView):
    queryset = Article.objects.filter(is_private=False, is_published=True)
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]


class PrivateArticleList(generics.ListAPIView):
    queryset = Article.objects.filter(is_private=True, is_published=True)
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class URLListView(generics.ListCreateAPIView):
    serializer_class = URLSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        url_patterns = []
        base_url = settings.SITE_URL if hasattr(settings, 'SITE_URL') else self.request.build_absolute_uri('/')

        for pattern in get_resolver().url_patterns:
            if hasattr(pattern, 'name') and pattern.name:
                url_pattern = force_str(pattern.pattern)
                full_url = base_url + url_pattern
                url_patterns.append({
                    'name': pattern.name,
                    'url': full_url
                })

        return url_patterns
