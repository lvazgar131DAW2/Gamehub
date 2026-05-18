from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
import re

class Game(models.Model):

    CATEGORY_CHOICES = [
        ('accion', 'Acción'),
        ('aventura', 'Aventura'),
        ('rpg', 'RPG'),
        ('estrategia', 'Estrategia'),
        ('deporte', 'Deporte'),
        ('simulacion', 'Simulación'),
        ('otro', 'Otro'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='games/', null=True, blank=True)
    trailer_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    release_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_average_rating(self):
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else 0

    def get_review_count(self):
        return self.reviews.count()

    @property
    def embed_url(self):
        if not self.trailer_url:
            return None

        patterns = [
            r'youtube\.com/watch\?v=([^\&\?]+)',
            r'youtu\.be/([^\&\?]+)',
            r'youtube\.com/shorts/([^\&\?]+)'
        ]

        for pattern in patterns:
            match = re.search(pattern, self.trailer_url)
            if match:
                video_id = match.group(1)
                return f'https://www.youtube.com/embed/{video_id}'

        return None