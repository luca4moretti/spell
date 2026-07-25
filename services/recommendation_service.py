class RecommendationService:

    def recommend(

        self,

        movies,

        minimum

    ):

        return [

            movie

            for movie in movies

            if movie.rating >= minimum

        ]
