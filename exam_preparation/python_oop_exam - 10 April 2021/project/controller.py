from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium = self.__validate_aquarium_type(aquarium_type, aquarium_name)
        if aquarium is None:
            return 'Invalid aquarium type.'
        self.aquariums.append(aquarium)
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):
        decoration = self.__validate_decoration_type(decoration_type)
        if decoration is None:
            return 'Invalid decoration type.'
        self.decorations_repository.add(decoration)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return
        self.decorations_repository.remove(decoration)
        aquarium.add_decoration(decoration)
        return f'Successfully added {decoration_type} to {aquarium_name}.'

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = self.__validate_fish_type(fish_type, fish_name, fish_species, price)
        if fish is None:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        fish_price = sum([f.price for f in aquarium.fish])
        decor_price = sum([d.price for d in aquarium.decorations])
        aquarium_price = fish_price + decor_price
        return f"The value of Aquarium {aquarium_name} is {aquarium_price:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'
        return result.strip()

    @staticmethod
    def __validate_aquarium_type(aquarium_type, aquarium_name):
        aquarium_types = {
            'FreshwaterAquarium': FreshwaterAquarium,
            'SaltwaterAquarium': SaltwaterAquarium,
        }
        if aquarium_type in aquarium_types:
            return aquarium_types[aquarium_type](aquarium_name)
        return None

    @staticmethod
    def __validate_decoration_type(decoration_type):
        decoration_types = {
            'Ornament': Ornament,
            'Plant': Plant
        }
        if decoration_type in decoration_types:
            return decoration_types[decoration_type]()
        return None

    @staticmethod
    def __validate_fish_type(fish_type, fish_name: str, fish_species: str, price: float):
        fish_types = {
            'FreshwaterFish': FreshwaterFish,
            'SaltwaterFish': SaltwaterFish,
        }
        if fish_type in fish_types:
            return fish_types[fish_type](fish_name, fish_species, price)
        return None

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None
