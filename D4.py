#SOCKETS PORT SCANNER AND FILE ORGANIZER
#SOCKETS ARE USED AS BLOCKS IN NETWORK COMMUNICATION
#socket.socket() - creates a brand-new unprogrammed socket
#bind() - claims a specific port number on your machine
#listen() - listening mode, waiting for someone to call
#accept() - Answers the incoming call and opens the communication line
#connect() - reaches out over the network to dial a listening server
#send()/recv() - transmits or catches bytes of data
import socket
print("-----NETWORK SOCK_STREAM INITIATION-----")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3.0)
target_ip = "192.168.56.104"
target_port = 80
try:
    print("attempting to connect to" + target_ip + ":" + str(target_port))
    s.connect((target_ip , target_port))
    print("CONNECTED")
except socket.timeout:
    print("TIMED OUT")
except Exception as e:
    print(f"ERROR: {e}")
finally:
    s.close()

