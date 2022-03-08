import pygame
from pygame.sprite import Sprite
class Ship(Sprite):

    def __init__(self, game_settings, screen):

        self.screen = screen

        super(Ship, self).__init__()
        
        # Load ship image
        self.image = pygame.image.load("C:/Users/19255/Documents/GitHub/Alien-Invasion/images/spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Ship position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement Flags
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.game_settings = game_settings

    # Draw ship to screen at current location
    def blitme(self):        
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.move_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.game_settings.ship_movement_speed
        elif self.move_left == True and self.rect.left > 0:
            self.rect.centerx -= self.game_settings.ship_movement_speed
        elif self.move_up == True and self.rect.top > 0 and self.rect.top < self.game_settings.screen_height:
            self.rect.centery -= self.game_settings.ship_movement_speed
        elif self.move_down == True and self.rect.bottom < self.game_settings.screen_height:
            self.rect.centery += self.game_settings.ship_movement_speed
    
    def center_ship(self):
        self.rect.bottom = self.screen_rect.bottom
        self.center = self.screen_rect.centerx