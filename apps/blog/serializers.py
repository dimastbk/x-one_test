from rest_framework import serializers

from apps.blog.models import BlogPage


class PageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    description = serializers.CharField(required=False)

    class Meta:
        fields = "__all__"
        model = BlogPage


class ShortPageSerializer(PageSerializer):
    class Meta:
        exclude = ("content",)
        model = BlogPage
