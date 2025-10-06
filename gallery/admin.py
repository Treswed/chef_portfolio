from django.contrib import admin
from .models import GalleryImage, Video

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured']
    search_fields = ['title', 'description']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'is_featured', 'created_at']
    list_filter = ['is_featured']
    search_fields = ['title', 'description']