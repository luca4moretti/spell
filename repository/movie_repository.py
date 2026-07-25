from models.movie import Movie
from data.sample_movies import MOVIES

class MovieRepository:

    def load(self):

        return [

            Movie(**movie)

            for movie in MOVIES

        ]
