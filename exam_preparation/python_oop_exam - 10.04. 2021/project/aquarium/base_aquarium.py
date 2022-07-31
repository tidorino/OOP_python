from abc import ABC, abstractmethod

from project.core.validator import Validator


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_str(value, 'Aquarium name cannot be an empty string.')
        self.__name = value

