from django.urls import path
from . import views

app_name = 'movies' # for namespacing must be called app_name

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail'),
]