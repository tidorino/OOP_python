from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):

    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        value_to_reduce_battery = self._calculate_battery_level(mileage, self.MAX_MILEAGE)
        self.battery_level -= value_to_reduce_battery

    @staticmethod
    def _calculate_battery_level(mileage, max_mileage):
        value = mileage / max_mileage
        return round(value * max_mileage)

    @property
    def type(self):
        return 'PassengerCar'
