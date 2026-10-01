#27 sep 2026 - DAY 32
#TCP VS UDP 
#The internet relies on main two primary protocols that are UDP AND TCP 
#TCP - It is a Certified phone call , you dial a number, the receiver answers, confirms they you, and only then do you start speaking. if they miss a sentence, you repeat it until every word and info is received correctly.
#UDP - It is a Live Radio Broadcast, The host speaks into the microphone and transmits immediately. if your radio glitches for half a second, you miss those words and there is no rewind but the transmission keeps working and streaming without interruption.



#TCP - TRANSMISSION CONTROL PROTOCOL - A RELIABLE HANDSHAKE
 #-Its is connection oriented, It gurantees that the data arrives sequentially and without missing any info or corruption it repeats data if it is missing through the connection.
  #-HOW TCP 3-WAY HANDSHAKE WORKS
  #-Before working any application and viewing its data a 3-Way TCP HANDSHAKE IS DEVLOPED THROUGH THE NETWORK SOCKET, TCP establishes a virtual connection via it and using flag bits.
#  -STEPS OF 3-WAY HANDSHAKE
#  -SYN - SYNCHRONIZE -The client sends a packet with the SYN flag set to an open port on the target server.So, it sends a packet to a open port so that a connection can be build between them.
#  -SYN-ACK - SYNCHRONIZE - ACKNOWLEDGE - If the port is open and listening the server reponds with both SYN AND ACK flags set so, it means the connection is active and formed between them.
#  -ACK ACKNOWLEDGE - The client responds with an ACK packet this confirms that yes THE connection is fully established.
#  -After this process an active socket pipeline opens enabling data Transmission or banner grabbing
  #-THIS PROVIDES:
#    :Sequence Tracking: every byte sent is tagged with a sequence number.
#    :Retransmissions:If a packet is lost in transit, the receiver detects the gap, and them TCP automatically repeats and retransmits that missing packet until it has being received correctly.
#    :Clean Closure:When the session betweem recevier and sender ends, TCP uses FIN flags to terminate the pipeline and release system socket resources.
#    :CORE TCP SERVICES ARE : 
#           :HTTP : PORT(80) - WEB BROWSING
#           :HTTPS: PORT(433)- WEB BROWSING


#           :SSH  : PORT(22) - ENCRYPTED REMOTE TERMINAL MANAGEMENT
#           :FTP  : PORT(21) - FILE TRANSFERS
#           :SMTP : PORT(25) - MAIL SERVER ROUTING

#UDP - USER DATAGRAM PROTOCOL - THE HIGH SPEED COURIER
# -HOW UDP WORKS:
#  -NO HANDSHAKE: UDP skips session establishment. The client sends datagrams immediately to the target IP and port without verifying if the receiver is ready or not.
#  -No Retransmission: UDP does not have retransmission if data is missed or corrupted it cannot be retransmitted
#  -Low Overhead and high Velocity: By omitting sequence numbers, connection tracking, and acknowledgement headers, UDP achieves higher speed and lower latency
#  -CORE SERVICES:
#  -UDP is selected for real-time services where delivery speed takes priority over occasional dropeed packets.
#    - DNS : PORT(53) :Resolving Domain names to IP addresses
#    - DHCP: Assigning dynamic IP Addresses on local networks
#    - VoIP AND Video Streaming: Live voice and video feeds
#    - Online Gaming: Real time Movement and action data
   
#THE CTF PORT bible - Core Service Ports
#  -During Security Auditing, pentesting and CTF Challenges, Services Enumerations these all start with mapping open ports to their default applications
#      21 - FTP - TCP - Check for anonymous Logins and ClearText Data.
#      22 - SSH - TCP - Secure Shell, Remote terminal access and audited for weak keys and brute-force flaws
#      23 - Telnet - TCP - Legacy unencrypted remote access , vulnerable due to plain-text credentials transmissions
#      53 - DNS - UDP/TCP - Domain Nmae System. Primary Target for zone transfers and cashe poisoning
#     80 - HTTP - TCP - Hypertext transfer protocol , unencrpted web traffic , target for web vulnerability testing
#      110 - POP3 - TCP - Post Office Protocol v3 Legacy mail retrieval service
#      143 - IMAP - TCP - Internet Message Access Protocol Interactive email Retrieval Service
#     443 - HTTPS - TCP - HTTP Secure, encrypted web traffic using SSL/TLS
#      445 - SMB - TCP - Server Message Block, Windows file sharing, primary target for exploits like eternal blue
#      3306 - MySQL - TCP - Relational database server , Audited for default admin credentials and remote access
#      3389 - RDP - TCP - Remote Desktop Protocol, Windows GUI access, tested for brute force attecks and RCE Flaws
#      8080 - HTTP-Alt - TCP Alternate Web  port commonly used for dev servers and web proxies like burpsuite

#WORK WITH WIRESHARK OR TCPDUMP AS IT Demostrates their architectural differences in live traffic captures 
