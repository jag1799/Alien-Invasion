import pygame
class Settings():

    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (150, 150, 255)

        self.ship_movement_speed = 1.0

        # Laser settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.max_bullets = 3

        pygame.display.set_caption("Alien Invasion")
