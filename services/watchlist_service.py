class WatchlistService:

    def unwatched(

        self,

        movies

    ):

        return [

            movie

            for movie in movies

            if not movie.watched

        ]
