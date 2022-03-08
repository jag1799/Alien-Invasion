import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, screen, game_settings):

        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's position
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        # Move the alien right
        self.x += self.game_settings.alien_speed * self.game_settings.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True