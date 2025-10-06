from django.contrib import admin
from .models import ChefProfile, Testimonial

@admin.register(ChefProfile)
class ChefProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'years_experience']
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'is_featured', 'created_at']
    list_filter = ['rating', 'is_featured']
    search_fields = ['name', 'content']