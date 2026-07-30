import csv


class CsvExporter:

    def export(self, movies, filename):

        with open(

            filename,

            "w",

            newline="",

            encoding="utf8"

        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                "Title",

                "Year",

                "Rating"

            ])

            for movie in movies:

                writer.writerow([

                    movie.title,

                    movie.year,

                    movie.rating

                ])
