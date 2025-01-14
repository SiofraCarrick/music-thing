#pip install python-vlc

import tkinter as tk

from time_label import TimeLabel
from vlc_player import VLCPlayer
from playback_controls import PlaybackControls


class MainApp:
    """Main application to combine all components."""
    def __init__(self, root):
        self.root = root
        self.root.title("VLC Music Player")
        self.root.geometry("800x480")
        self.root.configure(bg='#39395a')

        self.player = VLCPlayer()
        self.time_label_widget = tk.Label(self.root, text="00:00 / 00:00")
        self.time_label_widget.grid(row=3, column=0, columnspan=4, pady=10)

        self.controls = PlaybackControls(
            root,
            self.player,
            lambda current, duration: TimeLabel.update_time_label(self.time_label_widget, current, duration)
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
