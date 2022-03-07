import pygame
class Settings():

    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_movement_speed = 1.0
        self.max_ships = 3

        self.alien_speed = 0.25
        self.alien_drop_speed = 10.0
        self.fleet_direction = 1 # 1 = right, -1 = left

        # Laser settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.max_bullets = 3

        pygame.display.set_caption("Alien Invasion")
