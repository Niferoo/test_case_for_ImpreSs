from rest_framework import serializers
from .models import User, Article
from .validators import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'is_published', 'is_private', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']


class URLSerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.URLField()
