from django.shortcuts import render
from .models import GalleryImage, Video

def gallery_view(request):
    images = GalleryImage.objects.all()
    categories = GalleryImage.objects.values_list('category', flat=True).distinct()
    
    # Filter by category
    category = request.GET.get('category', '')
    if category:
        images = images.filter(category=category)
    
    context = {
        'images': images,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'gallery/gallery.html', context)

def videos_view(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'gallery/videos.html', context)