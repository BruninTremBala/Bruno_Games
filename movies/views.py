from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def list_movies(request):
    movie_list = Post.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'movies/index.html', context)

def detail_movie(request, movie_id):
    movie = get_object_or_404(Post, pk=movie_id)
    context = {"movie": movie}
    return render(request, "movies/detail.html", context)

def create_movie(request):
    if request.method == "POST":
        title = request.POST.get("title")
        genre = request.POST.get("genre")
        content = request.POST.get("content")
        poster_url = request.POST.get("poster_url")
        post_date = timezone.now()  # Definido automaticamente

        movie = Post(title=title, genre=genre, content=content, poster_url=poster_url, post_date=post_date)
        movie.save()
        return HttpResponseRedirect(reverse("movies:detail", args=(movie.pk,)))
    return render(request, "movies/create.html")

def update_movie(request, movie_id):
    movie = get_object_or_404(Post, pk=movie_id)
    if request.method == "POST":
        movie.title = request.POST.get("title")
        movie.genre = request.POST.get("genre")
        movie.content = request.POST.get("content")
        movie.poster_url = request.POST.get("poster_url")
        movie.save()
        return HttpResponseRedirect(reverse("movies:detail", args=(movie.id,)))
    context = {"movie": movie}
    return render(request, "movies/update.html", context)

def delete_movie(request, movie_id):
    movie = get_object_or_404(Post, pk=movie_id)
    if request.method == "POST":
        movie.delete()
        return HttpResponseRedirect(reverse("movies:index"))
    context = {"movie": movie}
    return render(request, "movies/delete.html", context)
