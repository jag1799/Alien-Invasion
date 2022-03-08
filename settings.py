import pygame
class Settings():

    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.max_ships = 3

        self.alien_speed = 0.25
        self.alien_drop_speed = 10.0
        self.fleet_direction = 1 # 1 = right, -1 = left

        # Laser settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.max_bullets = 3

        self.alien_speedup = 0.1
        self.ship_speed_scaler = 0.25
        self.bullet_speed_scaler = 0.5
        self.alien_point_scaler = 20

        self.initialize_dynamic_settings()

        pygame.display.set_caption("Alien Invasion")
    
    def initialize_dynamic_settings(self):

        self.ship_movement_speed = 1.0
        self.bullet_speed = 3.0
        self.alien_speed = 0.25
        self.fleet_direction = 1
        self.alien_points = 50
    
    def level_up(self):
        
        self.ship_movement_speed += self.ship_speed_scaler
        self.bullet_speed += self.bullet_speed_scaler
        self.alien_speed += self.alien_speedup
        self.alien_points += self.alien_point_scaler
        
        