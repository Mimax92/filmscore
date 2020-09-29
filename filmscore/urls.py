from django.urls import path, re_path
from .views import Allmovies, AddMovie, EditMovie, DelMovie, EditMovieExtra, MovieView

urlpatterns = [
    path('all/', Allmovies.as_view(), name="all-movies"),
    path('film/<int:pk>', MovieView.as_view(), name="movie-view"),
    path('add_film/', AddMovie.as_view(), name="add-movie"),
    path('edit_film/<int:pk>', EditMovie.as_view(), name="edit-movie"),
    path('edit_film/extra/<int:pk>', EditMovieExtra.as_view(), name="edit-movie-extra"),

    re_path(r'^(?P<pk>\d+)/del_movie/', DelMovie.as_view(), name="del-movie"),

]
