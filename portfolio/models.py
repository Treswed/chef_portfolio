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


class Visit(models.Model):
    """A simple request/visit log for viewing visitor activity in the admin.

    Note: keep this compact to avoid huge tables during heavy traffic. For
    production analytics consider an external service or async logging.
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=500)
    method = models.CharField(max_length=10)
    status_code = models.PositiveSmallIntegerField(null=True, blank=True)
    ip_address = models.CharField(max_length=45, blank=True)
    user = models.ForeignKey(
        'auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    user_agent = models.CharField(max_length=255, blank=True)
    referrer = models.CharField(max_length=500, blank=True)
    session_key = models.CharField(max_length=40, blank=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Site Visit'
        verbose_name_plural = 'Site Visits'

    def __str__(self):
        user = self.user.username if self.user else 'anonymous'
        return f"{self.timestamp.isoformat()} {self.path} ({user})"


class Statistic(models.Model):
    """Simple key/value statistic shown on the homepage.

    Example entries:
      key='recipes_created', label='Recipes Created', value=150, icon='🍳', order=1
    """
    key = models.SlugField(max_length=50, unique=True)
    label = models.CharField(max_length=120)
    value = models.BigIntegerField(default=0, help_text='Enter a whole number. Commas are allowed (e.g. 10,000).')
    icon = models.CharField(max_length=8, blank=True, help_text='Emoji or short icon text')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.label}: {self.value}"