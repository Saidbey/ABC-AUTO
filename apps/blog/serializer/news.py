from rest_framework import serializers

from apps.blog.model.news import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
