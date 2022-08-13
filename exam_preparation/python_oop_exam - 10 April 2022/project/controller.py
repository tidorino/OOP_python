class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player in self.players:
                continue
            self.players.append(player)
            added_players.append(player.name)
        return f'Successfully added: {", ".join(added_players)}'

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name, sustenance_type):
        player = self.__find_player_by_name(player_name)
        if player is None:
            return 
        supply = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            return

        for idx in range(len(self.supplies) - 1, -1, -1):
            current_supply = self.supplies[idx]

            if current_supply.__class__.__name__ == sustenance_type:
                if player.stamina == 100:
                    return f'"{player.name} have enough stamina.'
                player.stamina = min(player.stamina + current_supply.energy, 100)
                self.supplies.pop(idx)
                return f'{player.name} sustained successfully with {current_supply.name}.'
            continue

        raise Exception(f'There are no {sustenance_type.lower()} supplies left!')

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        error_message = ''
        if first_player.stamina == 0:
            error_message += f'Player {first_player.name} does not have enough stamina.'
        if second_player.stamina == 0:
            error_message += f'\nPlayer {second_player.name} does not have enough stamina.'
        if error_message:
            return error_message.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        # first duel:
        first_pl_damage = first_player.stamina / 2
        second_player.stamina = max(second_player.stamina - first_pl_damage, 0)
        if second_player.stamina == 0:
            return f'Winner: {first_player.name}'

        # second duel:
        second_pl_damage = second_player.stamina / 2
        first_player.stamina = max(first_player.stamina - second_pl_damage, 0)
        if first_player.stamina == 0:
            return f'Winner: {second_player.name}'

        if first_player.stamina > second_player.stamina:
            return f'Winner: {first_player.name}'
        return f'Winner: {second_player.name}'

    def next_day(self):
        for player in self.players:
            if player:
                player.stamina = max(player.stamina - player.age * 2, 0)
                self.sustain(player.name, 'Food')
                self.sustain(player.name, 'Drink')

    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'
        return result.strip()

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    def __find_supply_by_type(self, sustenance_type):
        if sustenance_type == 'Drink' or sustenance_type == 'Food':
            return sustenance_type
        return None

        # for idx in range(len(self.supplies) - 1, -1, -1):
        #     supply = self.supplies[idx]
        #     if supply.__class__._name__ == sustenance_type:
        #         return idx, supply
        # return -1, None