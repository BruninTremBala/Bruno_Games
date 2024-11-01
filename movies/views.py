from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Post, Comment, Category
from .forms import MovieForm
from django.utils import timezone


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'movies/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'movies/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all()  # Lista de posts na categoria
        return context

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            comment = Comment(
                post=post,
                author=request.user,
                text=text,
                created_date=timezone.now()
            )
            comment.save()
            return redirect('movies:detail', pk=post.id)
    return render(request, 'movies/review.html', {'post': post})


class MovieListView(generic.ListView):
    model = Post
    template_name = "movies/index.html"
    context_object_name = "movie_list"

class MovieDetailView(generic.DetailView):
    model = Post
    template_name = "movies/detail.html"

class MovieCreateView(generic.CreateView):
    model = Post
    form_class = MovieForm
    template_name = "movies/create.html"

    def get_success_url(self):
        return reverse_lazy("movies:detail", args=(self.object.pk,))

class MovieUpdateView(generic.UpdateView):
    model = Post
    form_class = MovieForm
    template_name = "movies/update.html"

    def get_success_url(self):
        return reverse_lazy("movies:detail", args=(self.object.pk,))

class MovieDeleteView(generic.DeleteView):
    model = Post
    template_name = "movies/delete.html"
    success_url = reverse_lazy("movies:index")

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

