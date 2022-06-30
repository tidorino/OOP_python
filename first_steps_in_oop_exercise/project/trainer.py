from OOP_Python.first_steps_in_oop_exercise.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return 'This pokemon is already caught'
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self,  pokemon_name: str):
        for pokemon in self.pokemon:
            if pokemon.name == pokemon_name:
                self.pokemon.remove(pokemon)
                return f'You have released {pokemon_name}'

        return 'Pokemon is not caught'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\n'
        result += f'Pokemon count {len(self.pokemon)}\n'

        for pokemon in self.pokemon:
            result += f'- {pokemon.pokemon_details()}' + '\n'

        return result.strip()

