from rest_framework import serializers

from apps.blog.models import BlogPage


class BlogPageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BlogPage
