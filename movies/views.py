from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import MovieForm


class MovieListView(generic.ListView):
    model = Post
    template_name = "movies/index.html"

def list_movies(request):
    movie_list = Post.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'movies/index.html', context)

def detail_movie(request, movie_id):
    movie = get_object_or_404(Post, pk=movie_id)
    context = {"movie": movie}
    return render(request, "movies/detail.html", context)


def search_movies(request):
    context = {}
    if request.GET.get("query", False):
        search_term = request.GET["query"].lower()
        movie_list = Post.objects.filter(name__icontains=search_term)
        context = {"movie_list": movie_list}
    return render(request, "movies/search.html", context)


def create_movie(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie = Post(**movie_form.cleaned_data)
            movie.save()
            return HttpResponseRedirect(reverse("movies:detail", args=(movie.pk,)))
    else:
        movie_form = MovieForm()
    context = {"movie_form": movie_form}
    return render(request, "movies/create.html", context)


def update_movie(request, movie_id):
    movie = get_object_or_404(Post, pk=movie_id)

    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie.title = form.cleaned_data["title"]
            movie.genre = form.cleaned_data["genre"]
            movie.content = form.cleaned_data["content"]
            movie.post_date = form.cleaned_data["post_date"]
            movie.poster_url = form.cleaned_data["poster_url"]
            movie.save()
            return HttpResponseRedirect(reverse("movies:detail", args=(movie.id,)))
    else:
        form = MovieForm(
            initial={
                "title": movie.title,
                "genre": movie.genre,
                "content": movie.content,
                "post_date": movie.post_date,
                "poster_url": movie.poster_url
            }
        )

    context = {"movie": movie, "form": form}
    return render(request, "movies/update.html", context)


def delete_movie(request, movie_id):
    movie = get_object_or_404(Post, pk=movie_id)

    if request.method == "POST":
        movie.delete()
        return HttpResponseRedirect(reverse("movies:index"))

    context = {"movie": movie}
    return render(request, "movies/delete.html", context)

