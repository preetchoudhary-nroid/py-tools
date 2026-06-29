#DAY - 11 - PACKET SNIFFER
#INSTALL scapy
#captures live packets on ur network interface
#READ ALL THE RAW PACKETS MOVING THROUGH THE WIRE.
#layer 1 - IP HEADER contains source ip and destination ip
#layer 2 - PROTOCOL HEADER data is TCP(web traffic/file downloads), UDP(video streaming,gaming)
#layer 3 - Payload ACTUAL DATA being transmitted
#ADMIN PERMISSIONS REQUIRED
import sys
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = "UNKNOWN"
        details = " "

        if packet.haslayer(TCP):
            proto= "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            details = f"Ports: {src_port} -> {dst_port}"

            if packet[TCP].payload:  #raw bytes to string
                raw_payload = bytes(packet[TCP].payload)
                payload_preview = "".join([chr(b) if 32 <= b < 127 else "." for b in raw_payload[:40]])
                #numbers between 32 and 127 are ASCII CHARS - chr(b) turns number to letter - if line break enter "."
        elif packet.haslayer(UDP):
            proto = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            details = f"Ports: {src_port} -> {dst_port}"

        elif packet.haslayer(ICMP):
            proto = "ICMP"
            details = f"Type: {packet[ICMP].type} | Code: {packet[ICMP].code}"

        print(f"[{proto}] {src_ip} -> {dst_ip} | {details}")

def start_sniffing(interface=None, filter_proto=None):
    print("=========================================")
    print("          PACKET SNIFFER ENGINE          ")
    print("=========================================")
    print(f"[*]Initializing Live capture Engine...")
    if filter_proto:
        print(f"[*] APPLYING BFP PROTOCOL FILTER: {filter_proto.lower()}")
    print("[*] Sniffing Active. Press CTRL + C TO STOP\n.")

    try:
        #sniff()  is the core scapy execution loop
        #filter: USES BERKELEY PACKET FILTER
        #prn: Dictates the callback function that processes every single packet captured
        #store = 0 : tells scapy NOT to save packets in RAM, preventing memory crashes
        sniff(iface=interface, filter=filter_proto, prn=process_packet, store=0)

    except KeyboardInterrupt:
        print("\n [*]Capture STOPPED by USER. EXITING CLEANLY.")
    except Exception as e:
        print(f"ERROR: FAILED TO ACCESS NETWORK INTERFACE: {e}")
        print("[!]NOTE: This script MUST RUN AS ADMINISTRATOR/ ROOT PRIVILEGES.")

if __name__ == "__main__":
    chosen_filter = input("Enter Protocol filter (TCP/UDP/ICMP or press enter for all:").strip().lower()

    if chosen_filter not in ["tcp","udp","icmp",""]:
        print("INVALID FILTER.Defaulting to capture all traffic.")
        chosen_filter = None
    elif chosen_filter == "":
        chosen_filter = None
    start_sniffing(filter_proto=chosen_filter)
