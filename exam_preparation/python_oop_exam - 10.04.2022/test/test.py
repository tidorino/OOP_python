from project.movie import Movie

from unittest import TestCase, main


class MovieTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('Movie', 2000, 4.5)

    def test_movie__is_initialized_correctly(self):
        self.assertEqual('Movie', self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(4.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_movie_name_empty_string_expect_to_rais(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertEqual('Name cannot be an empty string!', str(ex.exception))

    def test_movie_year_setter_if_year_is_valid_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886
        self.assertEqual('Year is not valid!', str(ex.exception))

    def test_add_actor__check_if_actor_is_in_actor_list(self):
        self.movie.add_actor('Actor')
        self.assertEqual(['Actor'], self.movie.actors)

    def test_add_actor__return_message_when_actor_is_already_in_actor_list(self):
        movie = Movie('Movie', 2000, 4.5)
        movie.actors = ['Actor']
        result = movie.add_actor('Actor')
        self.assertEqual('Actor is already added in the list of actors!', result)

    def test_rating_if_grater_than_other_movie_rating(self):
        other = Movie('Movie2', 2012, 3)
        result = self.movie.__gt__(other)
        expected_result = '"Movie" is better than "Movie2"'
        self.assertEqual(expected_result, result)

    def test_rating_if_its_lower_than_other_movie_rating(self):
        other = Movie('Movie2', 2012, 5)
        result = self.movie.__gt__(other)
        expected_result = '"Movie2" is better than "Movie"'
        self.assertEqual(expected_result, result)

    def test_repr(self):
        result = repr(self.movie)
        expected = f"Name: {self.movie.name}\nYear of Release: {self.movie.year}\nRating: {self.movie.rating:.2f}\n" \
                   f"Cast: {', '.join(self.movie.actors)}"
        self.assertEqual(expected, result)


if __name__ == '__main':
    main()
