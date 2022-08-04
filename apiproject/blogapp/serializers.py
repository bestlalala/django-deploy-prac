from rest_framework import serializers
from .models import Blog

# 글 작성에 사용
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'body')

# 글 목록에 사용
class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'summary')