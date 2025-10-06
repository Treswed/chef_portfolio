from django.db import models

class ChefProfile(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='chef/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    
    # Social Media
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    
    # Experience
    years_experience = models.IntegerField(default=0)
    specialties = models.TextField(help_text="Comma-separated specialties")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Chef Profile"
        verbose_name_plural = "Chef Profile"


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.rating} stars"

    class Meta:
        ordering = ['-created_at']