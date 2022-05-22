
from multiprocessing import context
from unicodedata import category
from django.http import StreamingHttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import View

from .models import Movie, Genre, Category

# def get_list_video(request):
#     return render(request, 'movies/movie.html', {'video_list': Video.objects.all()})

# def get_video(request, pk: int):
#     _video = get_object_or_404(Video, id=pk)

#     return render(request, 'movies/movie.html', {"video": _video})

# def get_streaming_video(request, pk: int):
#     file, status_code, content_length, content_range = open_file(request, pk)
#     response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

#     response['Accept-Ranges'] = 'bytes'
#     response['Content-Length'] = str(content_length)
#     response['Cache-Control'] = 'no-cache'
#     response['Content-Range'] = content_range
#     return response

class ShowMovie(DetailView):
    model = Movie
    template_name = 'movies/movie.html'
    context_object_name = 'movie'
    slug_field = 'url'
    

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        last_add = Movie.objects.all()

        context['categories'] = categories
        context['last_add'] = last_add
        
        return context

class ShowAuth(ListView):
    model = Movie
    template_name = 'movies/auth.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Авторизация'
    #     return context  


class RedirectIndexView(View):
    def get(self, request):
        return redirect('/')


class MoviesView(View):
    def get(self, request, category_id):
        last_add = Movie.objects.all()
        movies = last_add.filter(category=category_id)
        genres = Genre.objects.all()
        categories = Category.objects.all()
        
        cat_selected = category_id

        context = {'movies_list': movies,
                   'genres': genres , 
                   'title': 'Фильмы', 
                   'category': category_id,
                   'categories': categories,
                   'cat_selected': cat_selected,
                   'last_add': last_add,
                   }

        return render(request, "movies/movies.html", context=context)


class ShowFilmsView(View):
    def get(self, request, ):
        movies = Movie.objects.all()
        genres = Genre.objects.all()
        categories = Category.objects.all()
        last_add = movies
        cat_selected = 0

        context = {'movies_list': movies,
                   'genres': genres, 
                   'cat_selected': cat_selected,
                   'categories': categories,
                   'last_add': last_add,
                
                   }

        return render(request, "movies/index.html", context=context)


    # def get_queryset(self):
    #     return render(request, "movies/index.html", {'movies_list': movies, 'genres': genres , 'title': 'Фильмы'})
