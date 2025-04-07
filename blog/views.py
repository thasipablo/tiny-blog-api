from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
  # permission_classes = [IsAuthenticated]
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer

  @action(detail=True, methods=['post'])
  def like(self, request, pk=None):
    post = self.get_object()
    post.likes += 1
    post.save()
    return Response({'likes': post.likes})
