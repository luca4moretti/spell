import json

class JsonExporter:

    def export(

        self,

        movies,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                [

                    movie.__dict__

                    for movie

                    in movies

                ],

                file,

                indent=4

            )
