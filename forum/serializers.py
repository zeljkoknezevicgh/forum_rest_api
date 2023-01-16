from rest_framework import serializers
from .models import Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = Post
        fields = ("id", "title", "body", "created_at", "user")
        read_only_fields = ("id", "created_at",)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = Comment
        fields = ("text","created_at", "user")
        read_only_fields = ("created_at",)