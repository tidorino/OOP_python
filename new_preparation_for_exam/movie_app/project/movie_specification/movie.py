from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):
    MIN_YEAR_OF_MOVIE = 1888

    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
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
        if len(value) == 0:
            raise ValueError('The title cannot be empty string!')
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < self.MIN_YEAR_OF_MOVIE:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not type(value).__name__ == 'User':
            raise ValueError('The owner must be an object of type User!')
        self.__owner = value

    @property
    def type(self):
        return

    @abstractmethod
    def details(self):
        pass


