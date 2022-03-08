

class GameStats():

    def __init__(self, game_settings) -> None:
        self.game_settings = game_settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()
    
    def reset_stats(self):
        self.remaining_ships = self.game_settings.max_ships
        self.score = 0
        self.level = 1
