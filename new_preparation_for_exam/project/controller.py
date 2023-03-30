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
        pass

    def duel(self, first_player_name, second_player_name):
        pass

    def next_day(self):
        pass

    def __str__(self):
        return ''

