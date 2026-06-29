#DIR BRUTER - JUST A REGULAR BRUTE FORCER TO FIND HIDDEN FILES IN A WEBSITE DIRECTORIES
from http.client import responses

import requests
import sys
def brute_force_dirs(target_url):
    if not target_url.endswith("/"):
        target_url += "/"
    print(f"\n[*]Target URL: {target_url}")
    print("[+] Loading path discovery engine...")
    print("="*50)

    wordlist = [
        "admin", "login", "dashboard", "api", "config",
        "backup", "secret", "images", "robots.txt", "phpinfo.php"
    ]
    found_count = 0
    for path in wordlist:
        full_url = f"{target_url}{path}"
        try:
            response = requests.get(full_url, timeout=3, headers={"User-Agent":"SecurityAudioBot/1.0"})
            if response.status_code == 200:
                print(f"FOUND - 200 OK  --->{full_url}")
                found_count += 1
            elif response.status_code == 301 or response.status_code == 302:
                print(f"REDIRECT - 301 or {response.status_code} -----{full_url}")
                found_count += 1
            elif response.status_code == 403:
                print(f"FORBIDDEN -403 ---{full_url} (Directory exists but restricted")
                found_count += 1
        except requests.exceptions. RequestException as e:
            print(f"[-]ERROR ON {full_url}: {e}")
            continue

    print("="*60)
    print(f"[+]Scan Completed. Identified {found_count} active paths.")
if __name__ == "__main__":
        print("===============================================")
        print("          WEB PATH DISCOVERY UTILITY           ")
        print("===============================================")

        url_input = input("\n ENTER TARGET URL(http://example.com)")
        if url_input:
            brute_force_dirs(url_input)
        else:
            print("\n ERROR: NO TARGET URL SPECIFIED")
