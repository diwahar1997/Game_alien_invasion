import sys
import pygame
from setting import Settings 
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien 

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    
    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion Game")
    #make a ship
    ship = Ship(ai_settings,screen)
    #make the alien
    alien = Alien(ai_settings,screen)
    # Make a group to store bullets .
    bullets = Group()
    # Make a group to alien.
    aliens = Group()
    
    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Set the background colour 
    bg_color = (230,230,230)
    #start the main loop for the game
    while True:
        #watch for the keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship,aliens,bullets)
        
run_game()