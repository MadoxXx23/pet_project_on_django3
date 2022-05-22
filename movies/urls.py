from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShowFilmsView.as_view()),
    path("index.html", views.RedirectIndexView.as_view()),
    path("auth.html", views.ShowAuth.as_view()),
    path("movies/<int:category_id>/", views.MoviesView.as_view(), name='category'),
    path("movies/<slug:slug>/", views.ShowMovie.as_view(), name='film'),
   
]