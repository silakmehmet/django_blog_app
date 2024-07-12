from rest_framework import serializers

from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id",)


class PostSerializer(serializers.ModelSerializer):

    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id", "created_date", "updated_date")

    def get_category_name(self, obj):
        return obj.category_id.name
