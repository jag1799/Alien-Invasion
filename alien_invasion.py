import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

# Opens a simple window
def run_game():

    # Initialize the game and create a window object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height), pygame.RESIZABLE)

    # Start player
    ship = Ship(game_settings, screen)


    bullets = Group()

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()

        # Update & delete bullets
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, bullets)

run_game()