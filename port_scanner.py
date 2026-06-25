#SIMPLE MULTIPLE PORT SCANNER (NMAP)
import socket
from datetime import datetime
print("-----CYBERSECURITY AUTOMATED PORT SCANNER")
target_ip = input("Enter TARGET IP: ")
start_port = int(input("Enter START PORT: "))
end_port = int(input("Enter END PORT: "))

services = {
    21 : "FTP",
    22 : "SSH",
    80 : "HTTP",
    443 : "HTTPS"
}
timestamp = datetime.now().strftime("%Y--%m--%d--%H--%M--%S")
filename = f"scan_report_{timestamp}.txt"

print(f"\n[!] Initializing scan on target: {target_ip}")
print(f"[!] Saving results on local file: {filename}")
print("-" * 50)

with open(filename, "w") as report:
    header = f"PORT SCAN REPORT ON TARGET: {target_ip}\n Date: {timestamp}\n" + ("-" * 50) + "\n"
    print(header, end="")
    report.write(header)

    for port in range(start_port , end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)

        try:
            result = s.connect_ex((target_ip, port))       #CONNECT_EX IS USED SO IT DOES NOT CRASH IF PORT IS CLOSED

            if result == 0:
                service_name = services.get(port,"Unknown service")
                output_line = f"[+] Port {port:<5} | STATUS:OPEN | SERVICE: {service_name}\n"
            else:
                output_line = f"[-] Port {port:<5} | STATUS: CLOSED\n"

            print(output_line, end="")
            report.write(output_line)
        except Exception as e:
            error_line = f"[-] Error scanning port {port:<5} | ERROR: {e}"
            print(error_line, end="")
            report.write(error_line)
        finally:
            s.close()

    footer = "\n" + ("-" * 50) + "\n SCAN SUCCESSFULLY TERMINATED. \n"
    print(footer)
    report.write(footer)
