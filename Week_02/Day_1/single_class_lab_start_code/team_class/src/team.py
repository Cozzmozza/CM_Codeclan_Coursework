class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.new_player = new_player
        self.players.append(new_player)
    
    def has_player(self, player_name):
        self.player_name = player_name
        for player in self.players:
            if player == player_name:
                return True
        return False

    def play_game(self, win):
        self.win = win
        if win == True:
            self.points += 3