from pygame import mixer


class Mixer:
    """Class for handling music and sounds."""

    def __init__(self, ai_game):
        """Init settings and load resources."""
        self.settings = ai_game.settings

        # Since sound on/off flag should be very dynamic,
        #   we preload sounds in case they would be needed at
        #   any point in time.
        self.laser_shot = mixer.Sound('music/laser_shot.wav')
        self.alien_crashed = mixer.Sound('music/alien_crashed.wav')
        self.game_over = mixer.Sound('music/game_over.wav')

    def play_music(self):
        """Starts to play background music."""
        if self.settings.sound_on:
            mixer.music.load('music/game_music_alien.wav')
            mixer.music.set_volume(self.settings.music_volume)
            # Play perpetually, until turned off
            mixer.music.play(-1)

    def stop_music(self):
        """Stops background music."""
        mixer.music.stop()

    def play_laser_shot(self):
        """Plays laser shot sound when bullet is fired."""
        if self.settings.sound_on:
            self.laser_shot.play()

    def stop_laser_shot(self):
        """Stops playing laser shot sound when bullet is fired."""
        self.laser_shot.stop()

    def play_alien_crashed(self):
        """Plays sound when aliens is shot down."""
        if self.settings.sound_on:
            self.alien_crashed.play()

    def stop_alien_crashed(self):
        """Stops playing sound when aliens is shot down."""
        self.alien_crashed.stop()

    def play_game_over(self):
        """Plays sound when game is over."""
        if self.settings.sound_on:
            self.game_over.play()