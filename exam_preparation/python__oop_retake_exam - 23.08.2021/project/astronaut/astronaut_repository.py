from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        astro = self.__get_astronaut_by_name(astronaut)
        if astro is None:
            self.astronauts.append(astro)

    def remove(self, astronaut: Astronaut):
        astronaut = self.__get_astronaut_by_name(astronaut)
        if astronaut:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        astronaut = self.__get_astronaut_by_name(name)
        if astronaut:
            return astronaut

    def __get_astronaut_by_name(self, astronaut):
        for astro in self.astronauts:
            if astro.name == astronaut.name:
                return astro
            return
