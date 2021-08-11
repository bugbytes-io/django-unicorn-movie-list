from django_unicorn.components import UnicornView, QuerySetType
from movies.models import Movie

class MovielistView(UnicornView):
    name: str = ''
    movies: QuerySetType[Movie] = Movie.objects.none()

    def mount(self):
        """ On mount, populate the movies property w/ a QuerySet of all movies """
        self.movies = Movie.objects.all()
        print(self.movies)

    def add_movie(self):
        """ Create the new movie, get new list of all movies, and clear the 'name' property """
        Movie.objects.create(name=self.name)
        self.movies = Movie.objects.all()
        self.name = ''

    def delete_all(self):
        """ Delete all movies and reset 'movies' property """
        Movie.objects.all().delete()
        self.movies = Movie.objects.none()