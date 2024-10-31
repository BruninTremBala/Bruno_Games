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
        movie_list = Post.objects.filter(title__icontains=search_term)  # Alterado para usar 'title'
        context = {"movie_list": movie_list}
    return render(request, "movies/search.html", context)



def create_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return HttpResponseRedirect(reverse("movies:detail", args=(movie.pk,)))
    else:
        form = MovieForm()

    context = {"form": form}
    return render(request, "movies/create.html", context)


def update_movie(request, movie_id):
    movie = get_object_or_404(Post, pk=movie_id)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("movies:detail", args=(movie.id,)))
    else:
        form = MovieForm(instance=movie)

    context = {"form": form, "movie": movie}
    return render(request, "movies/update.html", context)


def delete_movie(request, movie_id):
    movie = get_object_or_404(Post, pk=movie_id)
    if request.method == "POST":
        movie.delete()
        return HttpResponseRedirect(reverse("movies:index"))

    context = {"movie": movie}
    return render(request, "movies/delete.html", context)

