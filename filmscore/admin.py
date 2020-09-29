from django.contrib import admin
from .models import Film, ExtraInfo, Rating, Actor


# Register your models here.
# admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["title", "imdb_rating", "year"]
    list_filter = ("year",)
    search_fields = ("title", "description")

admin.site.register(ExtraInfo)
admin.site.register(Rating)
admin.site.register(Actor)