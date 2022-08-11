from unittest import TestCase, main

from project.library import Library


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library('Library')

    def test_init__if_valid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual('Name cannot be empty string!', str(ex.exception))

    def test_init__correct(self):
        self.assertEqual('Library', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_add_book_if_given_author_not_exist(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book('author2', 'title2')
        self.assertEqual({'author2': ['title2']}, self.library.books_by_authors)

    def test_add_book_if_given_author_exist(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book('author2', 'title2')
        self.assertEqual({'author2': ['title2']}, self.library.books_by_authors)
        self.library.add_book('author2', 'title3')
        self.assertEqual({'author2': ['title2', 'title3']}, self.library.books_by_authors)

    def test_add_reader_if_name_not_exist(self):
        self.library.add_reader('reader1')
        self.assertEqual({'reader1': []}, self.library.readers)

    def test_add_reader_if_name_exist(self):
        self.library.add_reader('reader1')
        self.assertEqual({'reader1': []}, self.library.readers)
        result = self.library.add_reader('reader1')
        expected = f'reader1 is already registered in the {self.library.name} library.'
        self.assertEqual(expected, result)

    def test_rent_book_first_if_reader_not_exist(self):
        self.assertEqual({}, self.library.readers)
        result = self.library.rent_book('reader1', 'author1', 'title1')
        expected = f'reader1 is not registered in the {self.library.name} Library.'
        self.assertEqual(expected, result)

    def test_rent_book_if_book_author_not_added(self):
        self.library.readers = {'reader1': []}
        self.library.books_by_authors = {'author1': ['title2']}
        result = self.library.rent_book('reader1', 'author1', 'title1')
        expected = f'{self.library.name} Library does not have author1\'s "title1".'
        self.assertEqual(expected, result)

    def test_rent_book_if_reader_author_title_exist(self):
        self.library.readers = {'reader1': []}
        self.library.books_by_authors = {'author1': ['title2']}
        self.library.rent_book('reader1', 'author1', 'title2')
        expected = {'reader1': [{'author1': 'title2'}]}
        result = self.library.readers
        self.assertEqual(expected, result)

    def test_rent_book__check_title_index_is_correct(self):
        pass


if __name__ == "__main__":
    main()
