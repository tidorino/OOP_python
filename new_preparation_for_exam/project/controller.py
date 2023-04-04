from project.player import Player


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
        # self.supplies.extend(supplies)

    def sustain(self, player_name, sustenance_type):
        player = self.__find_player_by_name(player_name)
        if player is None:
            return
        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return
        idx, supply = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            raise Exception(f'There are no {sustenance_type.lower()} supplies left!')
        if not player.need_sustenance:
            raise Exception(f'{player.name} have enough stamina.')
        player.stamina = min(player.stamina + supply.energy, Player.MAX_STAMINA)
        self.supplies.pop(idx)

        return f'{player_name} sustained successfully with {supply.name}.'

    def duel(self, first_player_name, second_player_name):
        pass

    def next_day(self):
        pass

    def __str__(self):
        return ''

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, - 1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return idx, supply





