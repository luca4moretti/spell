class StatisticsService:

    def build(

        self,

        movies

    ):

        watched = sum(

            movie.watched

            for movie in movies

        )

        average = round(

            sum(

                movie.rating

                for movie in movies

            ) / len(movies),

            2

        )

        return {

            "count": len(movies),

            "watched": watched,

            "average": average

        }
