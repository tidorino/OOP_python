from testing_lab.app.car_manager import Car

from unittest import TestCase, main


class CarTest(TestCase):
    CAR = 'BMW'
    MODEL = 'I3'
    FUEL_CONSUMPTION = 6
    FUEL_CAPACITY = 60

    def setUp(self) -> None:
        self.car = Car(self.CAR, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

    def test_is_initialized_correctly(self):
        self.assertEqual('I3', self.car.model)
        self.assertEqual('BMW', self.car.make)
        self.assertEqual(6, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_init_make(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_init_make_setter(self):
        new_value = 'Skoda'
        self.car.make = new_value
        self.assertEqual(new_value, self.car._Car__make)

    def test_init_model(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_init_model_setter(self):
        new_value = 'Octavia'
        self.car.model = new_value
        self.assertEqual(new_value, self.car._Car__model)

    def test_init_setter_fuel_consumption_negative_or_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_init_fuel_consumption(self):
        new_value = 8
        self.car.fuel_consumption = new_value
        self.assertEqual(new_value, self.car._Car__fuel_consumption)

    def test_init_setter_fuel_capacity_negative_or_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_init_fuel_capacity(self):
        new_value = 80
        self.car.fuel_capacity = new_value
        self.assertEqual(new_value, self.car._Car__fuel_capacity)

    def test_init_setter_fuel_amount_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -9
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_init_fuel_amount(self):
        new_value = 20
        self.car.fuel_amount = new_value
        self.assertEqual(new_value, self.car._Car__fuel_amount)

    def test_refuel_car_cannot_refill_zero_or_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel_add_fuel_to_fuel_amount(self):
        self.car.fuel_amount = 10
        self.car.refuel(10)
        result = self.car.fuel_amount
        self.assertEqual(20, result)

    def test_refuel_fuel_amount_equal_to_capacity(self):
        self.car.fuel_amount = 50
        self.car.refuel(20)
        self.assertEquals(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_if_not_enough_fuel_expect_to_raise(self):
        self.car.fuel_amount = 10
        with self.assertRaises(Exception) as ex:
            self.car.drive(200)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_if_enough_fuel(self):
        self.car.fuel_amount = 20
        self.car.drive(200)
        self.assertEqual(8, self.car.fuel_amount)


if __name__ == '__main__':
    main()
