import tkinter as tk
from tkinter import filedialog
from threading import Thread
import time


class PlaybackControls:
    """Manages the playback control buttons and progress bar."""
    def __init__(self, root, player, update_time_label_callback):
        self.root = root
        self.player = player
        self.update_time_label_callback = update_time_label_callback
        self.update_progress_flag = False

        self.create_widgets()
        self.progress_thread = Thread(target=self.update_progress)
        self.progress_thread.daemon = True

    def create_widgets(self):
        # Load MP3 Button
        self.load_button = tk.Button(self.root, text="Load MP3", command=self.load_mp3, width=12)
        self.load_button.grid(row=0, column=0, padx=10, pady=10)

        # Play Button
        self.play_button = tk.Button(self.root, text="Play", command=self.play, width=12)
        self.play_button.grid(row=0, column=1, padx=10)

        # Pause Button
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause, width=12)
        self.pause_button.grid(row=0, column=2, padx=10)

        # Stop Button
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop, width=12)
        self.stop_button.grid(row=0, column=3, padx=10)

        # Volume Slider
        self.volume_slider = tk.Scale(
            self.root, from_=0, to=100, orient="horizontal", label="Volume", command=self.set_volume
        )
        self.volume_slider.set(50)  # Set default volume to 50%
        self.volume_slider.grid(row=1, column=0, columnspan=4, pady=10)

        # Progress Bar
        self.progress = tk.Scale(
            self.root, from_=0, to=100, orient="horizontal", length=300, label="Progress", command=self.seek
        )
        self.progress.grid(row=2, column=0, columnspan=4, pady=10)

        # Time Label
        self.time_label = tk.Label(self.root, text="00:00 / 00:00")
        self.time_label.grid(row=3, column=0, columnspan=4, pady=10)

    def load_mp3(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            self.player.load_media(file_path)
            self.stop()  # Stop any ongoing playback before loading a new file
            self.progress.set(0)

    def play(self):
        self.player.play()
        self.update_progress_flag = True
        if not self.progress_thread.is_alive():
            self.progress_thread.start()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
        self.update_progress_flag = False
        self.progress.set(0)
        self.update_time_label_callback(0, 0)

    def set_volume(self, volume):
        self.player.set_volume(volume)

    def seek(self, percentage):
        self.player.seek(float(percentage))

    def update_progress(self):
        """Continuously update the progress bar and time label."""
        while True:
            if self.update_progress_flag and self.player.is_playing():
                current_time = self.player.get_time()
                duration = self.player.get_duration()

                if duration > 0:
                    progress = (current_time / duration) * 100
                    self.progress.set(progress)
                    self.update_time_label_callback(current_time, duration)

            time.sleep(0.5)
