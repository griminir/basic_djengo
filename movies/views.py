from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here. Are like controllers in MVC


def index(request):
    movies = Movie.objects.all()
    # select * from movies_movie
    # Movie.objects.filter(release_year=2013)
    # select * from movies_movie where release_year = 2013
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # can also use primary key as pk instead of id
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
