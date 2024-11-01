from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Post


class MovieForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "genre",
            "content",
            "post_date",
            "poster_url",
            "categories"
        ]
        labels = {
            "title": "Título",
            "genre" : "Gênero",
            "content" : "Conteúdo",
            "post_date": "Data da postagem",
            "poster_url": "URL do Poster",
            "categories": "Categorias"
        }
        widgets = {
            'categories': CheckboxSelectMultiple(),  # Exibe as categorias como uma lista de checkboxes
        }


