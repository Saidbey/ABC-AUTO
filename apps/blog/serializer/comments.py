from rest_framework import serializers

from apps.blog.model.comments import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
