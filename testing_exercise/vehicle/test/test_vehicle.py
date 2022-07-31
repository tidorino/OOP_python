from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    FUEL = 100
    HORSE_POWER = 2.5
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_vehicle__is_initialized_correctly(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive__not_enough_fuel_expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(120)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive__enough_fuel_and_decrease_fuel_after_consumption(self):
        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance
        self.vehicle.drive(distance)
        expected_result = self.FUEL - fuel_needed
        actual_result = self.vehicle.fuel
        self.assertEqual(expected_result, actual_result)

    def test_refuel__more_fuel_than_capacity_expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel__adding_fuel_to_available_fuel(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount
        self.vehicle.refuel(fuel_amount)
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_final_string_message(self):
        actual_result = str(self.vehicle)
        expected_result = f"The vehicle has {self.HORSE_POWER} horse power with {self.FUEL}" \
                          f" fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
