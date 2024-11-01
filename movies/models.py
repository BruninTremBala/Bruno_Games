from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)# Título da postagem
    content = models.TextField()              # Conteúdo em HTML
    post_date = models.DateTimeField(default=timezone.now)  # Data da postagem
    poster_url = models.URLField(max_length=200, null=True)
    def __str__(self):
        return self.title

User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']  # Ordena os comentários do mais recente para o mais antigo

    def __str__(self):
        return f"Comentário de {self.author} em {self.post}"