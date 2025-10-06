from django.shortcuts import render
from .models import ChefProfile, Testimonial
from recipes.models import Recipe
from gallery.models import GalleryImage, Video
from blog.models import BlogPost

def home(request):
    chef = ChefProfile.objects.first()
    featured_recipes = Recipe.objects.filter(is_featured=True)[:3]
    testimonials = Testimonial.objects.filter(is_featured=True)[:6]
    recent_posts = BlogPost.objects.filter(is_published=True)[:3]
    
    context = {
        'chef': chef,
        'featured_recipes': featured_recipes,
        'testimonials': testimonials,
        'recent_posts': recent_posts,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    chef = ChefProfile.objects.first()
    context = {'chef': chef}
    return render(request, 'portfolio/about.html', context)

def contact(request):
    chef = ChefProfile.objects.first()
    context = {'chef': chef}
    return render(request, 'portfolio/contact.html', context)