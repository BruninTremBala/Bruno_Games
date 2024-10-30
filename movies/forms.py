from django.forms import ModelForm
from .models import Post, Review, Provider


class MovieForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "post_date",
            "poster_url"
        ]
        labels = {
            "title": "Título",
            "content" : "Conteúdo",
            "post_date": "Data da postagem",
            "poster_url": "URL do Poster",
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            "author",
            "text",
        ]
        labels = {
            "author": "Usuário",
            "text": "Resenha",
        }


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = [
            "service",
            "has_flat_price",
            "price",
        ]
        labels = {
            "service": "Serviço de Streaming",
            "has_flat_price": "FLAT?",
            "price": "Preço",
        }
