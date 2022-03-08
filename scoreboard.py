import pygame.font
from ship import Ship
from pygame.sprite import Group

class ScoreBoard():

    def __init__(self, game_settings, screen, stats) -> None:
        self.game_settings = game_settings
        self.screen = screen
        self.stats = stats

        self.screen_rect = screen.get_rect()
        self.text_color = (30, 30, 30)
        self.text_font = pygame.font.SysFont(None, 48)

        self.prep_score(stats.score)
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    

    def prep_score(self, new_score):

        if self.stats.game_active:
            new_score = self.stats.score
        # Convert the score integer to a string for rendering
        score_str = str(self.stats.score)

        # Render a score image
        self.score_image = self.text_font.render(score_str, True, self.text_color, self.game_settings.bg_color)

        # Position the score text/image
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top + 20
    
    def draw_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    
    def prep_high_score(self):
        high_score = round(self.stats.high_score)

        high_score_str = str(high_score)
        self.high_score_image = self.text_font.render(high_score_str, True, self.text_color, self.game_settings.bg_color)
        
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 5
    
    def prep_level(self):
        # Convert the score integer to a string for rendering
        level_str = str(self.stats.level)

        # Render a score image
        self.level_image = self.text_font.render(level_str, True, self.text_color, self.game_settings.bg_color)

        # Position the score text/image
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.screen_rect.top + 60
    
    def prep_ships(self):

        self.ships = Group()

        for ship_num in range(self.stats.remaining_ships):
            ship = Ship(self.game_settings, self.screen)
            ship.rect.x = 10 + ship_num * (ship.rect.width + 5)
            ship.rect.y = 10
            self.ships.add(ship)
