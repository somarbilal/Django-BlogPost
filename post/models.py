# Create a model that represents a blog post, with fields such as title, body, author, and date published.
# Then create views and templates to display a list of blog posts, as well as a detailed view for each post.


# To create a model for a blog post in Django, you can use the models.
# Model class to define a new model class with fields such as title, body, author, and date published.
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField()

