from django.contrib import admin
from .models import BlogPost

# admin.site.register(BlogPost)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')

admin.site.register(BlogPost, BlogPostAdmin)

