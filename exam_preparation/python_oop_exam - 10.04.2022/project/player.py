class Player:
    UNIQUE_PLAYER_NAMES = []
    MINIMUM_AGE = 12
    DEFAULT_STAMINA = 100
    MAX_STAMINA = 100
    MIN_STAMINA = 0

    def __init__(self, name, age, stamina=DEFAULT_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Name not valid!')
        if value in self.UNIQUE_PLAYER_NAMES:
            raise Exception(f'Name {value} is already used!')
        self.UNIQUE_PLAYER_NAMES.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MINIMUM_AGE:
            raise ValueError('The player cannot be under 12 years old!')
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.MIN_STAMINA or value > self.MAX_STAMINA:
            raise ValueError('Stamina not valid!')
        self.__stamina = value
        
    @property
    def need_sustenance(self):
        return self.stamina < self.MAX_STAMINA
        # if self.stamina <= self.MAX_STAMINA:
        #     return True

    def __str__(self):
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}'
