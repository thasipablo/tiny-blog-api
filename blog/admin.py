from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('title', 'published_date')
  search_fields = ('title', 'content')
  list_filter = ('published_date',)
