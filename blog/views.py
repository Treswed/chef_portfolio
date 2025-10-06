from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    context = {'posts': posts}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    post.views += 1
    post.save()
    
    recent_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/blog_detail.html', context)