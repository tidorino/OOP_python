from project.planet.planet import Planet


class PlanetRepository:

    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        planet = self.__get_planet_by_name(planet)
        if planet is None:
            self.planets.append(planet)

    def remove(self, planet: Planet):
        planet = self.__get_planet_by_name(planet)
        if planet:
            self.planets.remove(planet)

    def find_by_name(self, name):
        planet = self.__get_planet_by_name(name)
        if planet:
            return planet

    def __get_planet_by_name(self, planet):
        for pl in self.planets:
            if pl.name == planet.name:
                return pl
            return

