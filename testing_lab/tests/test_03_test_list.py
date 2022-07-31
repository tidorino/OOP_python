from testing_lab.app.list import IntegerList

from unittest import TestCase, main


class IntegerListTest(TestCase):
    def test_is_initialized_correctly_without_data(self):
        integer = IntegerList()

        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_type_data(self):
        integer = IntegerList()

        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_integers_data(self):
        integer = IntegerList(2, 'asd')

        self.assertEqual([2], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(2, 'asd')
        self.assertEqual([2], integer._IntegerList__data)

        result = integer.get_data()
        self.assertEqual([2], result)

    def test_add__when_type_is_not_integer_expect_to_raise(self):
        integer = IntegerList('asd', 12.3)

        with self.assertRaises(ValueError) as ex:
            integer.add(integer)
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add__when_type_is_integer(self):
        integer = IntegerList(12)
        self.assertEqual([12], integer._IntegerList__data)

        integer.add(3)
        self.assertEqual([12, 3], integer._IntegerList__data)

    def test_remove_index__when_idx_is_not_in_data_expect_to_raise(self):
        integer = IntegerList(12, 2, 'asd', 34)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(5)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_remove_index__removes_element_from_data(self):
        integer = IntegerList(12)
        integer.remove_index(0)
        self.assertEqual(0, len(integer._IntegerList__data))
        # or : self.assertEqual([], integer._IntegerList__data)

    def test_remove_index__and_return_removed_element(self):
        integer = IntegerList(12)
        result = integer.remove_index(0)
        self.assertEqual(12, result)

    def test_get__when_idx_is_invalid_expect_to_raise(self):
        integer = IntegerList(12, 2, 'asd', 34)

        with self.assertRaises(IndexError) as ex:
            # Greater than the length index
            integer.get(5)
        self.assertEqual('Index is out of range', str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            # Equal of the length of the index
            integer.get(4)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get__and_return_element_with_provided_index(self):
        integer = IntegerList(12, 2, 14)
        result = integer.get(2)
        self.assertEqual(14, result)

    def test_insert__when_idx_is_invalid_expect_to_raise(self):
        integer = IntegerList(12, 2, 'asd', 34)

        with self.assertRaises(IndexError) as ex:
            # Greater than the length index
            integer.insert(5, 4)
        self.assertEqual('Index is out of range', str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            # Equal of the length of the index
            integer.insert(4, 4)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert__when_element_is_not_integer_expect_to_raise(self):
        integer = IntegerList(12, 2, 'asd', 34)
        # integer.insert(2, 'asd')
        # self.assertEqual()

        with self.assertRaises(ValueError) as ex:
            integer.insert(1, 'asd')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert__adds_element(self):
        integer = IntegerList(12, 2, 34)
        integer.insert(2, 4)
        self.assertEqual([12, 2, 4, 34], integer._IntegerList__data)

    def test_get_biggest__element(self):
        integer = IntegerList(12, 2, 34, -2, 345, -90)
        result = integer.get_biggest()
        self.assertEqual(345, result)

    def test_get_index__of_given_element(self):
        integer = IntegerList(12, 2, 34)
        result = integer.get_index(2)
        self.assertEqual(1, result)


if __name__ == '__main__':
    main()
