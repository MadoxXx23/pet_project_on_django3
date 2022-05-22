from django.contrib import admin
from .models import Category, Genre, Movie, Video, Actor, Rating, RatingStar, Reviews

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Video)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)

