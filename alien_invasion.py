from os import stat
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

# Opens a simple window
def run_game():

    # Initialize the game and create a window object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height), pygame.RESIZABLE)

    # Start player
    ship = Ship(game_settings, screen)

    bullets = Group()
    aliens = Group()

    stats = GameStats(game_settings)
    play_button = Button(game_settings, screen, "Press to Play")

    scoreboard = ScoreBoard(game_settings, screen, stats)

    # Initialize alien fleet
    gf.create_fleet(game_settings, screen, aliens, ship)

    while True:

        gf.check_events(game_settings, screen, ship, bullets, play_button, stats, aliens, scoreboard)

        if stats.game_active == True:

            ship.update()

            # Update & delete bullets
            gf.update_bullets(game_settings, screen, ship, aliens, bullets, stats, scoreboard)
            gf.update_aliens(game_settings, aliens, ship, stats, screen, bullets, scoreboard)

        gf.update_screen(game_settings, screen, ship, aliens, bullets, play_button, stats, scoreboard)

run_game()