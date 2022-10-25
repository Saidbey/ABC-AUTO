from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

# projects
from apps.blog.model.comments import Comment
from apps.blog.serializer.comments import CommentSerializer


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by('id')
    serializer_class = CommentSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']