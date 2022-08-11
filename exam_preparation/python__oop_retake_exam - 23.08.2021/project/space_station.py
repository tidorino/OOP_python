from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.new_astro_repository = AstronautRepository()
        self.new_planet_repository = PlanetRepository()

    def add_astronaut(self,astronaut_type: str, name: str):
        valid_astronaut_type = self.__validate_type(astronaut_type)
        if not valid_astronaut_type:
            raise Exception('Astronaut type is not valid!')
        valid_astronaut_name = self.__valid_given_name(name)
        if valid_astronaut_name:
            return f'{name} is already added.'
        new_astronaut = type(astronaut_type)(name)
        self.new_astro_repository.astronauts.append(new_astronaut)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self,name: str, items: str):
        planet = self.__valid_planet_name(name)
        if planet:
            return f'{name} is already added.'
        new_planet = Planet(name)
        new_planet.items.append(items)
        self.new_planet_repository.planets.append(new_planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        astro = self.__valid_given_name(name)
        if not astro:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.new_astro_repository.astronauts.remove(astro)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for astro in self.new_astro_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.__valid_planet_name(planet_name)
        if not planet:
            raise Exception('Invalid planet name!')


    def report(self):
        pass

    @staticmethod
    def __validate_type(astronaut_type):
        valid_type = [
            "Biologist",
            "Geodesist",
            "Meteorologist"
        ]
        if astronaut_type in valid_type:
            return True
        return False

    def __valid_given_name(self, name):
        for astronaut in self.new_astro_repository.astronauts:
            if astronaut.name == name:
                return True
        return False

    def __valid_planet_name(self, name):
        for planet in self.new_planet_repository.planets:
            if planet.name == name:
                return True
        return False
