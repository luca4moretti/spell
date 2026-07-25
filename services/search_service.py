class SearchService:

    def by_genre(

        self,

        movies,

        genre

    ):

        return [

            movie

            for movie in movies

            if movie.genre == genre

        ]
