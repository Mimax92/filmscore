from django.db import models
from datetime import date


class ExtraInfo(models.Model):
    TYPE = {
        (0, 'Other'),
        (1, 'Comedy'),
        (2, 'Action'),
        (3, 'Horror'),
        (4, 'Family'),
        (5, 'Sci-Fi'),
        (6, 'Fantasy'),
        (7, 'Drama'),

    }
    runtime = models.PositiveSmallIntegerField(default=0)
    genres = models.PositiveSmallIntegerField(default=0, choices=TYPE)

    def __str__(self):
        return self.genres_title()

    def genres_title(self):
        return '{} {}'.format(self.genres, self.runtime)


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    extra_data = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.year_title()

    def year_title(self):
        return '{} {}'.format(self.title, self.year)


class Rating(models.Model):
    review = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=3)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class Actor(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    year_of_birth = models.DateField(default=date.today)
    films = models.ManyToManyField(Film)
