from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here. Are like controllers in MVC


def index(request):
    movies = Movie.objects.all()
    # select * from movies_movie
    # Movie.objects.filter(release_year=2013)
    # select * from movies_movie where release_year = 2013
    return render(request, 'index.html', {'movies': movies})
