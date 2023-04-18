from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    ERROR_MSG_BRAND = 'Brand cannot be empty!'
    ERROR_MSG_MODEL = 'Model cannot be empty!'
    ERROR_MSG_LICENSE_PLATE_NUMBER = 'License plate number is required!'

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not value.strip():
            raise ValueError(self.ERROR_MSG_BRAND)
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError(self.ERROR_MSG_MODEL)
        self.__model = value

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        if not value.strip():
            raise ValueError(self.ERROR_MSG_LICENSE_PLATE_NUMBER)
        self.__license_plate_number = value

    @property
    def type(self):
        return

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        if not self.is_damaged:
            self.is_damaged = True
        self.is_damaged = False

    def __str__(self):
        if self.is_damaged:
            return f'"{self.brand} {self.model} ' \
                   f'License plate: {self.license_plate_number} ' \
                   f'Battery: {self.battery_level}% ' \
                   f'Status: Damaged'

        return f'"{self.brand} {self.model} ' \
               f'License plate: {self.license_plate_number} ' \
               f'Battery: {self.battery_level}% ' \
               f'Status: OK'
