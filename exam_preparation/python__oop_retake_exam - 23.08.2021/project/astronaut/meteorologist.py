from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    NEEDED_UNITS_OXYGEN = 15
    OXYGEN = 90

    def __init__(self,name: str):
        super().__init__(name, self.OXYGEN)

    def breathe(self):
        self.OXYGEN -= self.NEEDED_UNITS_OXYGEN
