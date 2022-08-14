from unittest import TestCase, main

from project.bookstore import Bookstore


class BookstoreTest(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_init_correct(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual(0, self.bookstore.total_sold_books)
        self.assertDictEqual({}, self.bookstore.availability_in_store_by_book_titles)

    def test_init_book_limit_setter_if_zero_or_less_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = 0
        self.assertEqual('Books limit of 0 is not valid', str(ex.exception))
        self.bookstore.books_limit = 1
        self.assertEqual(1, self.bookstore.books_limit)

    def test_number_of_book_in_store_valid_with_books_store_limit(self):
        self.bookstore.books_limit = 2
        self.bookstore.availability_in_store_by_book_titles = {'book1': 1}
        result = len(self.bookstore.availability_in_store_by_book_titles.values())
        self.assertEqual(1, result)
        result1 = len(self.bookstore)
        self.assertEqual(1, result1)

    def test_number_of_book_in_store_valid_with_books_store(self):
        self.bookstore.books_limit = 2
        self.bookstore.availability_in_store_by_book_titles = {'book1': 1}
        count_book = 0
        for num in self.bookstore.availability_in_store_by_book_titles.values():
            count_book += num

        self.assertEqual(1, count_book)

    def test_receive_book_if_not_enough_space_in_store_expect_to_raise(self):
        self.bookstore.books_limit = 5
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('title1', 6)
        self.assertEqual('Books limit is reached. Cannot receive more books!', str(ex.exception))

    def test_receive_book_if_book_title_not_in_store(self):
        self.bookstore.books_limit = 5
        result = self.bookstore.receive_book('title1', 0)
        self.assertEqual('0 copies of title1 are available in the bookstore.', result)
        self.assertDictEqual({'title1': 0}, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_if_book_title_is_in_store_add_number_of_copies_in_dict(self):
        self.bookstore.books_limit = 5
        self.bookstore.receive_book('title1', 0)
        self.assertDictEqual({'title1': 0}, self.bookstore.availability_in_store_by_book_titles)
        result = self.bookstore.receive_book('title1', 3)
        self.assertEqual('3 copies of title1 are available in the bookstore.', result)
        self.assertDictEqual({'title1': 3}, self.bookstore.availability_in_store_by_book_titles)

    def test_is_total_numb_books_correct(self):
        self.bookstore.books_limit = 5
        self.bookstore.receive_book('title1', 3)
        result = self.bookstore.availability_in_store_by_book_titles['title1']
        self.assertEqual(3, result)

    def test_sell_book_if_book_not_available_in_store_expect_to_raise(self):
        self.bookstore.books_limit = 5
        self.bookstore.availability_in_store_by_book_titles['title1'] = 1
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('title2', 1)
        self.assertEqual("Book title2 doesn't exist!", str(ex.exception))
        self.assertEqual({'title1': 1}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_if_not_enough_copies_of_book_in_store_expect_to_raise(self):
        self.bookstore.books_limit = 5
        self.bookstore.availability_in_store_by_book_titles['title1'] = 1
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('title1', 2)
            self.assertEqual("Book title1 has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_book_successfully(self):
        self.bookstore.books_limit = 5
        self.bookstore.__total_sold_books = 0
        self.bookstore.availability_in_store_by_book_titles['title1'] = 2
        result = self.bookstore.sell_book('title1', 1)
        expected = 'Sold 1 copies of title1'
        self.assertEqual(expected, result)
        self.assertDictEqual({'title1': 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(1, self.bookstore.total_sold_books)

    def test_str_info(self):
        self.bookstore.books_limit = 5
        book_title = 'title1'
        self.bookstore.__total_sold_books = 0
        self.bookstore.availability_in_store_by_book_titles[book_title] = 1
        self.bookstore.sell_book(book_title, 1)

        result = str(self.bookstore)
        expected = f"Total sold books: 1\n" \
                   f"Current availability: {len(self.bookstore)}\n" \
                   f" - {book_title}: 0 copies"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
