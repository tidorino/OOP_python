from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PainFactoryTest(TestCase):
    def setUp(self) -> None:
        self.pain_factory = PaintFactory('Name1', 40)

    def test_init_if_correct(self):

        self.assertEqual('Name1', self.pain_factory.name)
        self.assertEqual(40, self.pain_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pain_factory.valid_ingredients)
        self.assertEqual({}, self.pain_factory.ingredients)

    def test_add_ingredient__if_product_type_not_in_valid_ingredients_expect_to_raise(self):
        self.pain_factory.valid_ingredients = ['white', 'yellow']
        with self.assertRaises(TypeError) as ex:
            self.pain_factory.add_ingredient('blue', 6)
        self.assertEqual('Ingredient of type blue not allowed in PaintFactory', str(ex.exception))

    def test_add_ingredient__if_can_not_add_product_quantity_expect_to_raise(self):
        self.pain_factory.valid_ingredients = ['white', 'blue']
        self.pain_factory.add_ingredient('blue', 6)
        self.assertEqual(['white', 'blue'], self.pain_factory.valid_ingredients)
        self.pain_factory.ingredients = {'white': 10, 'green': 10, 'yellow': 15}
        with self.assertRaises(ValueError) as ex:
            self.pain_factory.add_ingredient('blue', 6)
        self.assertEqual('Not enough space in factory', str(ex.exception))

    def test_add_ingredient__if_can_add_product_quantity_who_exist_in_ingredients(self):
        self.pain_factory.ingredients = {'white': 10, 'blue': 10, 'yellow': 10}
        self.pain_factory.add_ingredient('blue', 6)
        result = self.pain_factory.ingredients
        self.assertEqual({'white': 10, 'blue': 16, 'yellow': 10}, result)

    def test_add_ingredient__if_can_add_product_quantity_who_does_not_exist_in_ingredients(self):
        self.pain_factory.ingredients = {'white': 10, 'blue': 10, 'yellow': 10}
        self.pain_factory.add_ingredient('red', 6)
        result = self.pain_factory.ingredients
        self.assertEqual({'white': 10, 'blue': 10, 'yellow': 10, 'red': 6}, result)

    def test_remove_ingredient__if_product_type_not_in_ingredients_expect_to_raise(self):
        self.pain_factory.ingredients = {'white': 10, 'blue': 10}
        with self.assertRaises(KeyError) as ex:
            self.pain_factory.remove_ingredient('red', 6)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient__if_product_type_in_ingredients_and_product_quantity_left_is_bigger_than_zero(self):
        self.pain_factory.ingredients = {'white': 10, 'blue': 10}
        self.pain_factory.remove_ingredient('blue', 3)
        self.assertEqual({'white': 10, 'blue': 7}, self.pain_factory.ingredients)

    def test_remove_ingredient__if_product_type_in_ingredients_and_product_quantity_left_is_less_than_zero_raise(self):
        self.pain_factory.ingredients = {'white': 10, 'blue': 10}
        with self.assertRaises(ValueError) as ex:
            self.pain_factory.remove_ingredient('blue', 13)
            self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_repr(self):

        self.pain_factory.ingredients = {'white': 10, 'blue': 10}
        result = repr(self.pain_factory)
        expected = 'Factory name: Name1 with capacity 40.\nwhite: 10\nblue: 10\n'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
