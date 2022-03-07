

class GameStats():

    def __init__(self, game_settings) -> None:
        self.game_settings = game_settings
        self.game_active = True
        self.reset_stats()
    
    def reset_stats(self):
        self.remaining_ships = self.game_settings.max_ships
