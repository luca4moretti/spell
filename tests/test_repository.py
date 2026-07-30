import unittest

from repository.movie_repository import MovieRepository


class RepositoryTests(unittest.TestCase):

    def test_repository_created(self):

        repository = MovieRepository()

        self.assertIsNotNone(repository)

    def test_empty_movies(self):

        repository = MovieRepository()

        self.assertEqual(

            len(repository.movies),

            0

        )


if __name__ == "__main__":

    unittest.main()
