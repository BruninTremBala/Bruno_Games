from django.urls import path

from . import views

app_name = "movies"
urlpatterns = [
    path("", views.list_movies, name="index"),
    path("create/", views.create_movie, name="create"),
    path("<int:movie_id>/", views.detail_movie, name="detail"),
    path("update/<int:movie_id>/", views.update_movie, name="update"),
    path("delete/<int:movie_id>/", views.delete_movie, name="delete"),
]
