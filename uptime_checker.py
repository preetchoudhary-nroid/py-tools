#MONITORING SCRIPT THAT VALIDATES WHETHER A LIST OF TARGETS ARE OPERATIONAL OR NOT
import requests
import time
TARGET_SITES = [
    "https://www.google.com",
    "https://www.github.com"
]
def check_uptime():
    print(f"\n[+]Running Uptime audit at {time.strftime('%Y-%m-%d %H-%M-%S')}...")
    print("="*50)

    for url in TARGET_SITES:
        try:
            response = requests.get(url, timeout=5, headers={"User-Agent": "UptimeBot/1.0"})

            if response.status_code == 200:
                status_label = "ONLINE / OK"
            elif response.status_code == 404:
                status_label = "NOT FOUND (404)"
            elif response.status_code == 403:
                status_label = "FORBIDDEN (403)"
            else:
                status_label = f"UNEXPECTED STATUS ({response.status_code})"
            print(f"[{status_label}]")
            print(f"     - Content type: {response.headers.get('Content-Type', 'Unknown')}")
            print(f"     - Status Engine: {response.headers.get('server','Hidden/Protected')}")
        except requests.exceptions.Timeout:
            print(f"[-]TIMEOUT {url} Took too long to respond")
        except requests.exceptions.ConnectionError:
            print(f"[-] OFFLINE {url} UNREACHABLE")
        except Exception as e:
            print(f"[-] ERROR {url}:{e}")
    print("="*50)

if __name__ == '__main__':
    print("[+]STARTING WEBSITE UPTIME MONITOR. PRESS CTRL + C TO TERMINATE.")
    try:
        while True:
            check_uptime()
            print("[+]Sleeping for 30 seconds Before the next Check!")
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n[*] Monitor Shutting Down. Cleanup Complete.")
