import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_setting,screen):
        "Initialize the alien and set the starting position"
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_setting=ai_setting
        
        
        #load the alien image and set its rect attribute.
        self.image =  pygame.image.load('images/spaceship.png') 
        self.rect = self.image.get_rect()
        
        #Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
        