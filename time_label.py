import time


class TimeLabel:
    """Handles the time label to display playback progress."""
    @staticmethod
    def update_time_label(label_widget, current_time, duration):
        current_time_str = time.strftime("%M:%S", time.gmtime(current_time))
        duration_str = time.strftime("%M:%S", time.gmtime(duration))
        label_widget.config(text=f"{current_time_str} / {duration_str}")