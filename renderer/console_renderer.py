from utils.rating import stars

class ConsoleRenderer:

    def display(

        self,

        movies,

        stats

    ):

        print()

        print("Movie Watchlist\n")

        for movie in movies:

            print(

                f"{movie.title}"

            )

            print(

                f"Genre: {movie.genre}"

            )

            print(

                f"Rating: {stars(movie.rating)}"

            )

            print(

                f"Watched: {movie.watched}"

            )

            print()

        print("Statistics\n")

        print(

            f"Movies: {stats['count']}"

        )

        print(

            f"Watched: {stats['watched']}"

        )

        print(

            f"Average rating: {stats['average']}"

        )
