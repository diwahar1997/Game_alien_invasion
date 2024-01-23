import random
class Settings():
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        "Initialize the game's settings."
        #Screen settings
        self.screen_width=1000
        self.screen_height =800
        self.bg_color=(self.color(),self.color(),self.color())   
        self.ship_speed_factor = 1.5 
        #bullet setting
        self.bullet_speed_factor = 1.5
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = self.color(), self.color(), self.color()
        self.bullets_allowed = 100
        
    def color(self):
        return random.randrange(1,230)
