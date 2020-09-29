from django.shortcuts import render
from django.views import View
from .models import Film, ExtraInfo, Rating
from django.shortcuts import redirect
from .forms import FilmForm, CreateUserForm, ExtraInfoForm, RatingForm
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, FilmSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class Allmovies(View):
    def get(self, request):
        films = Film.objects.all()

        ctx = {
            "movies": films
        }
        return render(request, "filmy.html", ctx)


class MovieView(View):
    def get(self, request, pk):
        film = get_object_or_404(Film, id=pk)
        extra_info = get_object_or_404(ExtraInfo, id=pk)
        rating = Rating.objects.filter(film=film)
        form_rating = RatingForm()
        ctx = {
            "film": film,
            "extra_info": extra_info,
            "rating": rating,
            "form_rating": form_rating,
        }
        return render(request, "show_film.html", ctx)

    def post(self, request, pk):
        form = RatingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            stars = form.cleaned_data["stars"]
            review = form.cleaned_data["review"]
            film = get_object_or_404(Film, id=pk)
            Rating.objects.create(stars=stars, review=review, film=film)
            return redirect(f"/films/film/{pk}")


class AddMovie(LoginRequiredMixin, View):

    def get(self, request):
        form = FilmForm()
        form_extra = ExtraInfoForm()
        return render(request, 'new_film.html', {"form": form, "form_extra": form_extra})

    def post(self, request):
        form = FilmForm(request.POST or None, request.FILES or None)
        form_extra = ExtraInfoForm(request.POST or None, request.FILES or None)
        if all((form.is_valid(), form_extra.is_valid())):
            form_extra.save()
            form.save()
            return redirect('all-movies')
        return render(request, 'new_film.html', {"form": form, "form_extra": form_extra})


class CreateUser(View):
    def get(self, request):
        form = CreateUserForm()
        ctx = {
            "form": form
        }
        return render(request, "create_user.html", ctx)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.cleaned_data.pop("repeated_password")
            user = get_user_model().objects.create_user(**form.cleaned_data)
            return redirect("/logout/")
        return render(request, "create_user.html", {"form": form})


class EditMovie(LoginRequiredMixin, UpdateView):
    model = Film
    fields = ["title", 'year', 'description', 'premiere', 'imdb_rating', 'poster']
    template_name = "edit_film.html"
    success_url = '/films/all/'


class DelMovie(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "filmscore.delate_film"
    model = Film
    template_name = "del_film.html"
    success_url = 'film_id'
    context_object_name = "movie"
    success_url = '/films/all/'


class EditMovieExtra(LoginRequiredMixin, UpdateView):
    model = ExtraInfo
    fields = ["genres", "runtime"]
    template_name = "edit_film_extra.html"
    success_url = '/films/all/'
