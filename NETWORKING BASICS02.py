#DAY 31 - IP ADDRESSING AND SUBNETTING
#IPv4 STRUCTURE IS A 32-Bit address divided into 4 octets - 192.168.1.1
#Private IP ranges - These are reserved for internal networks and do not travel across public internet safe from public hackers.
#-CLASS A - (10.0.0.0/8): For huge networks(16 million hosts)
#-CLASS B - (172.16.0.0/12):For medium networks(65,534 hosts)
#-CLASS C - (192.168.0.0/16):For Home networks(254 hosts per /24)
#Subnetting Basics: The slash notation(CIDR) defines the network size. A /24 (255.255.255.0) is the standard for most home and small office setups.
#NAT(Networking Address Translation): (HIDE INTERNAL IP OF A DEVICE) This is the "Gatekeeper" that allows an entire home network of private IPs to share a single public IP provided by your ISP
#To Divide a /24 network into 4 equal subnets, you must "borrow" 2 bits from the host portion (2 square = 4). This changes the subnet mask from /24 to /26(255.255.255.192).
#giving you 64 addresses (62 usable hosts) per subnet
#/24 - 255.255.255.0 - 24 bits , 8 bits for hosts
#/16 - 255.255.0.0  - 16 bits for the network, 16 bits for hosts
#/8 - 255.0.0.0 - 8 bits for the network, 24 bits for hosts

#SUBNETTING 192.168.1.0/24
#- 192.168.1.0 - RANGE - 192.168.1.1 - 192.168.1.62  - BROADCAST 192.168.1.63
#- 192.168.1.64 - RANGE - 192.168.1.65 - 192.168.1.126 - BROADCAST 192.168.1.127
#- 192.168.1.128 - RANGE - 192.168.1.129 - 192.168.1.190 - BROADCAST 192.168.1.191
#- 192.168.1.192 - RANGE - 192.168.1.193 - 192.168.1.254 - BROADCAST 192.168.1.255
