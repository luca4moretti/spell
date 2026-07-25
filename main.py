from config import EXPORT_FILE
from config import MIN_RATING

from repository.movie_repository import MovieRepository

from services.statistics_service import StatisticsService
from services.recommendation_service import RecommendationService

from renderer.console_renderer import ConsoleRenderer

from exporters.json_exporter import JsonExporter

movies = MovieRepository().load()

recommended = RecommendationService().recommend(

    movies,

    MIN_RATING

)

stats = StatisticsService().build(

    movies

)

ConsoleRenderer().display(

    recommended,

    stats

)

JsonExporter().export(

    movies,

    EXPORT_FILE

)
