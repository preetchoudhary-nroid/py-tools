#DAY 8 - SUBDOMAIN SCANNER #SUBDOMAIN_SCANNER
#CAN BE SAFELY RUN AGAINST ANY PUBLIC INTERACTION DOMAINS
#SUBDOMAINS ARE LIKE SIDE DOORS OR SPECIALIZED DEPARTMENTS
#eample.com - mail.example.com, vpn.example.com, dev.example.com
import socket
import time
def scan_subdomains(target_domain):
    print(f"\n[*]Target Domain: {target_domain}")
    print("[*]Initializing DNS Discovery Engine...")
    print("="*50)

    subdomain_wordlist = [
        "www", "mail", "ftp", "admin", "dev", "test",
        "api", "vpn", "blog", "shop", "status", "support"
    ]
    found_count = 0
    start_time = time.time()
    for sub in subdomain_wordlist:
        full_host = f"{sub}.{target_domain}"

        try:
            ip_address  = socket.gethostbyname(full_host)
            print(f"DISCOVERED -- {full_host:<25} | IP: {ip_address:<25}")
            found_count += 1
        except socket.gaierror:  #means DNS COULD NOT RESOLVE THE HOST NAME
            print("HOST NOT FOUND")
            continue
    duration = time.time() - start_time
    print("="*60)
    print(f"[+]Scan Completed. found {found_count} active subdomains in {duration:.4f} seconds")

if __name__ == "__main__":
    print("+"*60)
    print("SUBDOMAIN DISCOVERY ENGINE")
    print("+"*60)

    target = input("ENTER TARGET DOMAIN(github.com):").strip()
    if target:
        scan_subdomains(target)
    else:
        print("[!]ERROR: NO TARGET DOMAIN PROVIDED")

