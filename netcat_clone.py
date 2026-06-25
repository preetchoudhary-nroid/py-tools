"""
DAY 5 – NETCAT CLONE 
- Listen mode (-l) waits for connections.
- Client mode (-c IP:PORT) connects to a listener.
- Send messages, transfer files, execute remote commands.
- Use ONLY on your own machines.
"""

import socket
import subprocess
import os
import threading
import argparse

class NetcatClone:
    def __init__(self, host='0.0.0.0', port=4444):
        self.host = host
        self.port = port
        self.socket = None
        self.connections = []
        self.buffer_size = 4096

    # ---------- SERVER (FIXED) ----------
    def start_server(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
            self.socket.settimeout(1)   # 👈 crucial for breaking out of accept()
            print(f"[*] Listening on {self.host}:{self.port}")
            print("[*] Press Ctrl+C to stop the server.")

            while True:
                try:
                    client_sock, client_addr = self.socket.accept()
                except socket.timeout:
                    # Just loop again – this lets us catch Ctrl+C quickly
                    continue
                except (socket.error, KeyboardInterrupt) as e:
                    # On Windows, Ctrl+C raises socket.error with errno 10004
                    if isinstance(e, KeyboardInterrupt) or (isinstance(e, socket.error) and e.errno == 10004):
                        print("\n[*] Interrupted by Ctrl+C – shutting down...")
                        break
                    else:
                        print(f"[!] Socket error: {e}")
                        break

                # Got a client
                print(f"[+] Connection from {client_addr[0]}:{client_addr[1]}")
                self.connections.append(client_sock)
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_sock, client_addr)
                )
                client_thread.daemon = True
                client_thread.start()

        except KeyboardInterrupt:
            # Fallback catch (should not happen, but safe)
            print("\n[*] KeyboardInterrupt – shutting down...")
        except Exception as e:
            print(f"[!] Server error: {e}")
        finally:
            self.cleanup()

    # ---------- CLIENT ----------
    def start_client(self, target_host, target_port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((target_host, target_port))
            print(f"[+] Connected to {target_host}:{target_port}")

            recv_thread = threading.Thread(target=self.receive_messages)
            recv_thread.daemon = True
            recv_thread.start()

            while True:
                user_input = input()
                if user_input.lower() == '/quit':
                    self.socket.send('/quit'.encode('utf-8'))
                    break
                elif user_input.lower().startswith('/send '):
                    filename = user_input[6:].strip()
                    self.send_file(filename)
                elif user_input.lower().startswith('/cmd '):
                    command = user_input[5:].strip()
                    self.socket.send(f"cmd:{command}".encode('utf-8'))
                else:
                    self.socket.send(user_input.encode('utf-8'))

        except KeyboardInterrupt:
            print("\n[*] Disconnecting...")
        except ConnectionRefusedError:
            print("[!] Connection refused – is the server running?")
        except Exception as e:
            print(f"[!] Client error: {e}")
        finally:
            self.cleanup()

    def receive_messages(self):
        while True:
            try:
                data = self.socket.recv(self.buffer_size).decode('utf-8')
                if not data:
                    print("[!] Server disconnected.")
                    break
                print(f"\n[Server]: {data}")
            except Exception as e:
                print(f"[!] Error receiving: {e}")
                break

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
                    print(f"[*] Client {client_addr[0]} requested disconnection.")
                    break
                else:
                    print(f"\n[Message from {client_addr[0]}]: {data}")
            except ConnectionResetError:
                print(f"[!] Client {client_addr[0]} disconnected abruptly.")
                break
            except Exception as e:
                print(f"[!] Error handling client: {e}")
                break

        if client_sock in self.connections:
            self.connections.remove(client_sock)
        client_sock.close()
        print(f"[*] Client {client_addr[0]} disconnected.")

    # ---------- FILE TRANSFER ----------
    def send_file(self, filename):
        if not os.path.exists(filename):
            print(f"[!] File '{filename}' not found.")
            return
        try:
            with open(filename, 'rb') as f:
                file_data = f.read()
            header = f"FILE:{os.path.basename(filename)}:{len(file_data)}".encode('utf-8')
            self.socket.send(header + b'\n')
            self.socket.send(file_data)
            print(f"[+] File '{filename}' sent successfully.")
        except Exception as e:
            print(f"[!] Error sending file: {e}")

    def receive_file(self, client_sock):
        try:
            header = client_sock.recv(self.buffer_size).decode('utf-8')
            if not header.startswith('FILE:'):
                print("[!] Not a valid file transfer header.")
                return
            _, filename, filesize = header.strip().split(':')
            filesize = int(filesize)
            file_data = b''
            while len(file_data) < filesize:
                chunk = client_sock.recv(min(self.buffer_size, filesize - len(file_data)))
                if not chunk:
                    break
                file_data += chunk
            if len(file_data) != filesize:
                print("[!] File received incomplete.")
                return
            new_filename = f"received_{filename}"
            with open(new_filename, 'wb') as f:
                f.write(file_data)
            print(f"[+] File received and saved as '{new_filename}'.")
        except Exception as e:
            print(f"[!] Error receiving file: {e}")

    # ---------- COMMAND EXECUTION ----------
    def execute_command(self, command):
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.stdout:
                return f"[Output]\n{result.stdout}"
            elif result.stderr:
                return f"[Error]\n{result.stderr}"
            else:
                return "[+] Command executed successfully (no output)."
        except subprocess.TimeoutExpired:
            return "[!] Command timed out."
        except Exception as e:
            return f"[!] Error executing command: {e}"

    # ---------- CLEANUP ----------
    def cleanup(self):
        if self.socket:
            self.socket.close()
        for conn in self.connections:
            try:
                conn.close()
            except:
                pass
        print("[*] Cleanup complete.")


# ---------- MAIN ----------
def main():
    parser = argparse.ArgumentParser(description='Netcat Clone - Educational')
    parser.add_argument('-l', '--listen', action='store_true',
                        help='Run in listener (server) mode')
    parser.add_argument('-c', '--connect', help='Connect to IP:PORT (client)')
    parser.add_argument('-p', '--port', type=int, default=4444,
                        help='Port to use (default: 4444)')
    args = parser.parse_args()

    nc = NetcatClone(port=args.port)

    if args.listen:
        nc.start_server()
    elif args.connect:
        try:
            host, port = args.connect.split(':')
            nc.start_client(host, int(port))
        except ValueError:
            print("[!] Use IP:PORT format, e.g., 127.0.0.1:4444")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

