import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def update_screen(game_settings, screen, ship, aliens, bullets):

    # Redraw screen w/t color
    screen.fill(game_settings.bg_color)
    ship.blitme()

    # Draw alien
    aliens.draw(screen)

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

def update_bullets(aliens, bullets):
    
    # Update bullet sprites
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def bullet_keydown_event(bullets, event, game_settings, screen, ship):
    if event.key == pygame.K_SPACE:
        if len(bullets) < game_settings.max_bullets:
            new_bullet = Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)


def create_fleet(game_settings, screen, aliens, ship):

    # Create an alien and use its size to find the number of aliens
    # that fit in a row.  Then propagate it.
    alien = Alien(screen, game_settings)
    num_aliens = get_num_aliens(game_settings, alien.rect.width)
    num_rows = get_num_rows(game_settings, ship.rect.height, alien.rect.height)

    for row in range(num_rows):
        for new_alien in range(num_aliens):
            create_alien(game_settings, screen, aliens, new_alien, row)
    
def get_num_aliens(game_settings, alien_width):
    free_space = game_settings.screen_width - 2 * alien_width
    num_aliens = int(free_space / (2 * alien_width))
    return num_aliens

def get_num_rows(game_settings, ship_height, alien_height):
    free_y_space = (game_settings.screen_height - (3 * alien_height) - ship_height)
    num_rows = int(free_y_space / (2 * alien_height))
    return num_rows

def create_alien(game_settings, screen, aliens, alien_num, row_number):
    alien = Alien(screen, game_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)

def update_aliens(game_settings, aliens):
    check_fleet_edges(game_settings, aliens)
    aliens.update()

def check_fleet_edges(game_settings, aliens):

    # Check all aliens in the fleet
    for alien in aliens.sprites():
        if alien.check_edges() == True:
            change_fleet_direction(game_settings, aliens)
            break

def change_fleet_direction(game_settings, aliens):

    for alien in aliens.sprites():
        # Change the direction
        alien.rect.y += game_settings.alien_drop_speed
    game_settings.fleet_direction *= -1