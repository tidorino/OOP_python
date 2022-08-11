from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    OXYGEN = 50

    def __init__(self,name: str):
        super().__init__(name, self.OXYGEN)

    def breathe(self):
        self.OXYGEN -= self.NEEDED_UNITS_OXYGEN
