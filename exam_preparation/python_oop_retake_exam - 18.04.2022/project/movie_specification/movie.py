from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):
    MIN_YEAR = 1888
    MIN_AGE_RESTRICTION = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        #
        if len(value) == 0:
            raise ValueError('The title cannot be empty string!')
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < self.MIN_YEAR:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError('The owner must be an object of type User!')
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.MIN_AGE_RESTRICTION:
            raise ValueError(f'{self.__class__.__name__} movies must be restricted'
                             f' for audience under {self.age_restriction} years!')
        self.__age_restriction = value

    @abstractmethod
    def details(self):
        pass


