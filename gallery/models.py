from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Gallery Images"


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_url = models.URLField(help_text="YouTube or Vimeo URL")
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, help_text="e.g., 10:30")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_embed_url(self):
        """Convert YouTube/Vimeo URL to embed URL"""
        if 'youtube.com' in self.video_url or 'youtu.be' in self.video_url:
            if 'youtu.be' in self.video_url:
                video_id = self.video_url.split('/')[-1].split('?')[0]
            else:
                video_id = self.video_url.split('v=')[1].split('&')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif 'vimeo.com' in self.video_url:
            video_id = self.video_url.split('/')[-1]
            return f"https://player.vimeo.com/video/{video_id}"
        return self.video_url
    
    class Meta:
        ordering = ['-created_at']