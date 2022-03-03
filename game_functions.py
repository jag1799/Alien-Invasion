import sys
import pygame
from bullet import Bullet

def check_events(game_settings, screen, ship, bullets):

    # Respond to key presses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            
            # Update ship position
            ship_keydown_event(ship, event)

            # Add a bullet instance to the class & draw it to the screen.
            bullet_keydown_event(bullets, event, game_settings, screen, ship)
            
        
        elif event.type == pygame.KEYUP:
            ship_keyup_event(ship, event)

def update_screen(game_settings, screen, ship, bullets):

    # Redraw screen w/t color
    screen.fill(game_settings.bg_color)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make most recent updates visible
    pygame.display.flip()

def ship_keydown_event(ship, event):

    # Update ship position while key is down
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True

def ship_keyup_event(ship, event):

    # Stop ship update
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False

def update_bullets(bullets):
    
    # Update bullet sprites
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def bullet_keydown_event(bullets, event, game_settings, screen, ship):
    if event.key == pygame.K_SPACE:
        if len(bullets) < game_settings.max_bullets:
            new_bullet = Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)