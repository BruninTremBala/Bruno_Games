from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)# Título da postagem
    content = models.TextField()              # Conteúdo em HTML
    post_date = models.DateTimeField(default=timezone.now)  # Data da postagem
    poster_url = models.URLField(max_length=200, null=True)
    def __str__(self):
        return self.title