from project.horse_specification.horse import Horse


class Jockey:
    MIN_AGE = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # o	An instance of a Horse (child) class representing the horse taken by the jockey.
        # When a jockey is created in the app, he/she has NOT been given a horse yet.
        # o	The value should be set to None.
        # o	Keep in mind that one jockey can ride only one horse.
        self.horse: Horse.__class__.__name__ = None

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Name should contain at least one character!')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_AGE:
            raise ValueError('Jockeys must be at least 18 to participate in the race!')
        self.__age = value
