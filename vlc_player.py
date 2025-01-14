import vlc


class VLCPlayer:
    """Handles the VLC player functionality."""
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = None

    def load_media(self, file_path):
        self.media = self.instance.media_new(file_path)
        self.player.set_media(self.media)
        self.play()

    def play(self):
        if self.media:
            self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def set_volume(self, volume):
        self.player.audio_set_volume(int(volume))

    def seek(self, percentage):
        if self.media:
            duration = self.get_duration()
            new_time = (percentage / 100) * duration
            self.player.set_time(int(new_time * 1000))  # Set time in milliseconds

    def get_time(self):
        return self.player.get_time() / 1000  # Current time in seconds

    def get_duration(self):
        return self.player.get_length() / 1000  # Total duration in seconds

    def is_playing(self):
        return self.player.is_playing()
