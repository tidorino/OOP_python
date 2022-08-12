from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()
        self.successful_mission = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.__validate_astronaut_by_type(astronaut_type, name)
        if astronaut is None:
            raise Exception('Astronaut type is not valid!')

        valid_astronaut_name = self.__valid_given_name(name)
        if valid_astronaut_name:
            return f'{name} is already added.'
        self.astronaut_repository.add(astronaut)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'
        new_planet = Planet(name)
        new_planet.items = items.split(', ')
        self.planet_repository.add(new_planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):

        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception('Invalid planet name!')
        astronauts = self.__find_suitable_astronaut(5, 30)
        if len(astronauts) == 0:
            raise Exception('You need at least one astronaut to explore the planet!')

        sent_to_explore = 0

        for astronaut in astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
                sent_to_explore += 1
        if len(planet.items) == 0:
            self.successful_mission += 1
            return f'Planet: {planet_name} was explored. {sent_to_explore} astronauts participated in collecting items.'
        else:
            self.not_completed_missions += 1
            return 'Mission is not completed.'

    def report(self):
        result = ''
        result += f"{self.successful_mission} successful missions!\n" \
                  f"{self.not_completed_missions} missions were not completed!\n" \
                  f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n" \
                      f"Oxygen: {astronaut.oxygen}\n" \
                      f"Backpack items: " \
                      f"{'none' if len(astronaut.backpack) == 0 else ', '.join(astronaut.backpack)}\n"
        return result.strip()

    def __valid_given_name(self, name):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return True
        return False

    @staticmethod
    def __validate_astronaut_by_type(astronaut_type, name):
        astronaut_types = {
            'Biologist': Biologist,
            'Geodesist': Geodesist,
            'Meteorologist': Meteorologist,
        }
        if astronaut_type in astronaut_types:
            return astronaut_types[astronaut_type](name)
        return None

    def __find_suitable_astronaut(self, number_astronaut, min_oxygen):
        suitable_astronauts = []
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > min_oxygen:
                suitable_astronauts.append(astronaut)
        sorted_astronauts = sorted(suitable_astronauts, key=lambda x: -x.oxygen)[:number_astronaut]
        return sorted_astronauts



