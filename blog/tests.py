from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BlogPost


class BlogPostTests(APITestCase):
  def test_create_blogposr(self):
    """Test creating a blog post"""
    url = reverse("blog:blogposts")
    data = {
      "title": "Test Blog Post",
      "content": "This is a test blog post"
    }
    response = self.client.post(url, data, format="json")
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(BlogPost.objects.count(), 1)
    self.assertEqual(BlogPost.objects.get().title, "Test Blog Post")
