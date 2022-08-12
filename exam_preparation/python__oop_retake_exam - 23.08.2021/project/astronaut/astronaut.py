from abc import ABC, abstractmethod


class Astronaut(ABC):
    NEEDED_UNITS_OXYGEN = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Astronaut name cannot be empty string or whitespace!')
        self.__name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= self.NEEDED_UNITS_OXYGEN

    def increase_oxygen(self, amount):
        self.oxygen += amount

