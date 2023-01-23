# Then, you can use Django's views and templates to display a list of blog posts and a detailed view for each post.
# You can create a view function that retrieves a list of all blog posts from the database and passes them to a template to be rendered.


from django.shortcuts import render
from .models import BlogPost

def blog_post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_post_list.html', {'posts': posts})


# create a view function to handle the detailed view of each post
def blog_post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog_post_detail.html', {'post': post})



from django.shortcuts import redirect
from .forms import BlogPostForm

#for authentication and authorization
from django.contrib.auth.decorators import login_required #authentication
from django.core.exceptions import PermissionDenied #authorization

@login_required
def create_blog_post(request):
    if not request.user.has_perm('blog.add_blogpost'):
        raise PermissionDenied
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_post_detail', post_id=post.id)
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})


from django.shortcuts import get_object_or_404

def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if not request.user.has_perm('blog.change_blogpost', post):
        raise PermissionDenied
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_post_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
   
    return render(request, 'edit_blog_post.html', {'form': form, 'post_id': post.id})

def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if not request.user.has_perm('blog.delete_blogpost', post):
        raise PermissionDenied
    post.delete()
    return redirect('blog_post_list')

