from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = self.__horse_valid_by_type(horse_type, horse_name, horse_speed)
        for h in self.horses:
            if h.name == horse_name:
                raise Exception(f'Horse {horse_name} has been already added!')
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = self.__find_by_name(jockey_name)
        if jockey is None:

            jockey = Jockey(jockey_name, age)
            self.jockeys.append(jockey)
            return f'Jockey {jockey_name} is added.'
        else:
            raise Exception(f'Jockey {jockey_name} has been already added!')

    def create_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)
        for r in self.horse_races:
            if race == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = self.__find_horse_if_exist(horse_type)
        if horse is None:
            raise Exception(f'Horse breed {horse_type} could not be found!')
        if jockey.horse is None:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')
        #
        # jockey.horse = horse
        # return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)
        if race not in self.horse_races:
            raise Exception(f'Race {race_type} could not be found!')
        if len(race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

    @staticmethod
    def __horse_valid_by_type(horse_type, horse_name, horse_speed):
        horse_types = {"Appaloosa": Appaloosa,
                       "Thoroughbred": Thoroughbred}
        if horse_type in horse_types:
            return horse_types[horse_type](horse_name, horse_speed)
        # return None

    @staticmethod
    def __find_race_by_type(race_type):
        race_types = ["Winter",
                      "Spring",
                      "Autumn",
                      "Summer"]
        if race_type in race_types:
            return race_type

    def __find_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __find_horse_if_exist(self, horse_type):
        for horse in range(len(self.horses) - 1, - 1, - 1):
            if horse.__class__.__name__ == horse_type:
                return horse

        return None


