class Formatter:

    @staticmethod
    def movie(movie):

        return (

            f"{movie.title} "

            f"({movie.year}) "

            f"- Rating: {movie.rating}"

        )

    @staticmethod
    def separator():

        return "-" * 40
