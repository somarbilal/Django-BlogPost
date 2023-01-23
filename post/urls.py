# from django import views
from django.urls import path
# from .views import blog_post_list, blog_post_detail
from . import views

urlpatterns = [
    path('blog_post_list/', views.blog_post_list, name='blog_post_list'),
    # path('', blog_post_list, name='blog_post_list'),
    path('blog_post_detail/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('create_post/', views.create_blog_post, name='create_post'),
    path('edit_post/<int:post_id>/', views.edit_blog_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_blog_post, name='delete_post'),

]
