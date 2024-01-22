class Settings():
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        "Initialize the game's settings."
        #Screen settings
        self.screen_width=1000
        self.screen_height =800
        self.bg_color=(100,230,130)   
        self.ship_speed_factor = 1.5 
        #bullet setting
        self.bullet_speed_factor = 1.5
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = 30, 70, 60
        self.bullets_allowed = 100
