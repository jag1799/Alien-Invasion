import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, game_settings, screen, ship):
        
        # properly inherit from Sprite class
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Make bullet position a decimal
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.bullet_speed = game_settings.bullet_speed
    
    def update(self):

        self.y -= self.bullet_speed
        # Update rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
