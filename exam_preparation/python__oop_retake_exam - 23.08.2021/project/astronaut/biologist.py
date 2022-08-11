from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    NEEDED_UNITS_OXYGEN = 5
    OXYGEN = 70

    def __init__(self,name: str):
        super().__init__(name, self.OXYGEN)

    def breathe(self):
        self.OXYGEN -= self.NEEDED_UNITS_OXYGEN
