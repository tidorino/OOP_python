from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopsTests(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('PetShop')

    def test_pet_shop_init(self):
        name = 'PetShop'
        pet_shop = PetShop(name)

        self.assertEqual(name, pet_shop.name)
        self.assertEqual({}, pet_shop.food)
        self.assertEqual([], pet_shop.pets)

    def test_add_food_raises_when_qty_is_negative(self):
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food('Pet', -25)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food_adds_food_to_food_dict(self):
        food_name = 'food1'
        food_quantity = 50
        self.pet_shop.food = {}

        self.pet_shop.add_food(food_name, food_quantity)
        self.assertEqual({'food1': 50}, self.pet_shop.food)
        result = self.pet_shop.add_food(food_name, food_quantity)
        self.assertEqual(f'Successfully added 50.00 grams of food1.', result)

    def test_add_food_adds_food_qty_to_existing_food(self):
        food_name = 'food1'
        initial_qty = 100

        self.pet_shop.food[food_name] = initial_qty
        add_qty = 50
        result = self.pet_shop.add_food(food_name, add_qty)

        self.assertEqual('Successfully added 50.00 grams of food1.', result)
        self.assertTrue(food_name in self.pet_shop.food)
        self.assertEqual(initial_qty + add_qty, self.pet_shop.food[food_name])

    def test_add_pet__if_pet_name_is_in_pets_expect_to_raise(self):
        self.pet_shop.pets = ['pet2']
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('pet2')
        self.assertEqual('Cannot add a pet with the same name', str(ex.exception))

    def test_add_pet__if_pet_name_not_in_pets(self):
        self.pet_shop.pets = ['pet2']
        result = self.pet_shop.add_pet('pet1')
        self.assertEqual('Successfully added pet1.', result)

    def test_feed_pet__if_pet_name_not_in_pets_list_expect_to_raise(self):
        self.pet_shop.pets = ['pet2']
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('food1', 'pet1')
        self.assertEqual('Please insert a valid pet name', str(ex.exception))

    def test_feed_pet__if_food_name_not_in_food_list_expect_to_raise(self):
        self.pet_shop.food['food2'] = 0
        self.pet_shop.pets = ['pet2']
        result = self.pet_shop.feed_pet('food1', 'pet2')
        self.assertEqual('You do not have food1', result)

    def test_feed_pet__if_food_capacity_is_less_than_100(self):
        self.pet_shop.food['food2'] = 50
        self.pet_shop.pets.append('pet2')

        result = self.pet_shop.feed_pet('food2', 'pet2')
        self.assertEqual('Adding food...', result)
        self.assertEqual(50 + 1000.00, self.pet_shop.food['food2'])

    def test_feed_pet__if_food_capacity_is_more_than_100(self):
        self.pet_shop.food['food2'] = 165
        self.pet_shop.pets = ['pet2']

        result = self.pet_shop.feed_pet('food2', 'pet2')
        self.assertEqual('pet2 was successfully fed', result)
        self.assertEqual(65, self.pet_shop.food['food2'])

    def test_repr(self):
        self.pet_shop.pets = ['pet2', 'pet1']
        self.assertEqual(f'Shop {self.pet_shop.name}:\nPets: pet2, pet1', self.pet_shop.__repr__())


if __name__ == '__main__':
    main()

