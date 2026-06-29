#NETWORK INFO SCANNER OF A WEBSITE
#DNS LOOP UP - DOMAIN INTO PHYSICAL IP ADDRESS
#REVERSE DNS LOOP UP - FIND THE OFFICIAL HOSTNAME TIED TO THAT IP
#HTTP HEADER ANALYZER
#Targeted Port Scan
import socket
import urllib.request
class NetworkScanner:
    def __init__(self,domain):
        self.domain = domain
        self.ip_address = None
        self.reverse_hostname = None
        self.headers = {}
        self.open_ports = []

    def get_dns_info(self):
        print(f"[*]Resolving DNS for {self.domain}")
        try:
            self.ip_address = socket.gethostbyname(self.domain)
            try:
                self.reverse_hostname = socket.gethostbyaddr(self.domain)
            except socket.herror:
                self.reverse_hostname = "Unknown(Reverse DNS failed)"
        except socket.gaierror:
            print(f"[!]Error: Could NOT resolve{self.domain}")
    def get_http_headers(self):
        print(f"[*]Fetching HTTP headers for http://{self.domain}")
        try:
            url = f"http://{self.domain}"
            req = urllib.request.Request(url, headers={'USER-AGENT': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                for key, value in response.getheaders():
                    self.headers[key] = value
        except Exception as e:
             self.headers["Error"]=f"Could not fetch {self.domain}"
    def scan_common_ports(self):
        print("[*] Testing web server ports...")
        ports_to_test = [80,443] #80 - http , 443 - https
        for port in ports_to_test:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2.0)
            result = s.connect_ex((self.ip_address,port))
            if result == 0:
                self.open_ports.append(port)
            s.close()

    def generate_report(self):
        """Prints the compiled intelligence card cleanly."""
        # Safety Check: If DNS resolution failed completely, stop here.
        if self.ip_address is None:
            print("\n==================================================")
            print("[!] No Intelligence Data gathered. Scanner Failed.")
            print("==================================================\n")
            return

        print("\n" + "=" * 50)
        print(f"INTELLIGENCE REPORT FOR: {self.domain.upper()}")
        print("=" * 50)
        print(f"Target IP Address : {self.ip_address}")
        print(f"Reverse Hostname  : {self.reverse_hostname}")

        print("\n[+] Status of Web Ports:")
        for port in [80, 443]:
            status = "OPEN" if port in self.open_ports else "CLOSED"
            print(f"  - Port {port}: {status}")

        print("\n[+] Web Server Headers:")
        for key, val in self.headers.items():
            if key.lower() in ['server', 'date', 'content-type', 'connection', 'error']:
                print(f"  - {key}: {val}")
        print("=" * 50 + "\n")

if __name__ == "__main__":
    target_domain = input("ENTER TARGET DOMAIN(example.com):")
    scanner = NetworkScanner(target_domain)

    scanner.get_dns_info()
    if scanner.ip_address:
        scanner.get_http_headers()
        scanner.scan_common_ports()
        scanner.generate_report()






