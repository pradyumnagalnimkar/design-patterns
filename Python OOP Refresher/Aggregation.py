class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_player_info(self, number):
        for player in self.players:
            if number == player.number:
                return f"{player.name}({player.position})-{player.number}"
        return "Player not found."


player1 = Player("Kaka", 'AMF', 10)
player2 = Player("Neymar", 'RW', 7)
player3 = Player("Thiago Silva", 'CB', 6)
team = Team("Brazil")
team.add_player(player1)
team.add_player(player2)
team.add_player(player3)
print(team.get_player_info(6))

