class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Init game's settings."""
        # Window settings.
        self.caption = "Alien Invasion"

        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 191, 255)

        # Ship settings.
        self.ship_speed = 5
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings.
        self.alien_speed = 1.0
        # Fleet seetings.
        self.fleet_drop_speed = 10
        # Fleet direction: 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Game settings
        self.pause = 1.0 # seconds to pause after the ship was hit