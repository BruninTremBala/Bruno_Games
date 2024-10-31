from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.MovieListView.as_view(), name="index"),
    path("search/", views.search_movies, name="search"),
    path("create/", views.MovieCreateView.as_view(), name="create"),
    path("<int:pk>/", views.MovieDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", views.MovieUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.MovieDeleteView.as_view(), name="delete"),
]
