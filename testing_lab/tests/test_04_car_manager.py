from testing_lab.app.car_manager import Car

from unittest import TestCase, main

from testing_lab.app.car_manager import Car


class CarTest(TestCase):
    def setUp(self) -> None:
        self.car = Car(make='BMW', model='I3', fuel_consumption=6, fuel_capacity=200)

    def test_is_initialized_correctly(self):
        # self.assertEqual('I3', self.car.model)
        # self.assertEqual('BMW', self.car.make)
        self.assertEqual(6, self.car.fuel_consumption)
        self.assertEqual(200, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)


if __name__ == '__main__':
    main()