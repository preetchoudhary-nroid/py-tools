#DAY 10 - LOG ANALYZER
#AUTO READS MASSIVE FILES TO FIND OUT WHO IS SCANNING FOR VULNER. AND WHO IS TRYING TO CRASH THE SITE.
#count request per ip // track error // high requests per sec(brute force)
import re
from collections import Counter, defaultdict
from datetime import datetime
def generate_fake_logs():
    sample_logs = [
        '192.168.1.5 - - [29/Jun/2026:15:00:01 +0000] "GET /index.html HTTP/1.1" 200 4523',
        '192.168.1.5 - - [29/Jun/2026:15:00:02 +0000] "GET /about.html HTTP/1.1" 200 2105',
        # Attacker 1: Doing a directory scan (Lots of 404s)
        '10.0.0.99 - - [29/Jun/2026:15:00:03 +0000] "GET /admin HTTP/1.1" 404 230',
        '10.0.0.99 - - [29/Jun/2026:15:00:04 +0000] "GET /config.bak HTTP/1.1" 404 230',
        '10.0.0.99 - - [29/Jun/2026:15:00:05 +0000] "GET /secret.txt HTTP/1.1" 404 230',
        # Attacker 2: High-speed flood (Multiple requests in the exact same second)
        '172.16.0.4 - - [29/Jun/2026:15:00:10 +0000] "POST /login HTTP/1.1" 403 120',
        '172.16.0.4 - - [29/Jun/2026:15:00:10 +0000] "POST /login HTTP/1.1" 403 120',
        '172.16.0.4 - - [29/Jun/2026:15:00:10 +0000] "POST /login HTTP/1.1" 403 120',
        '172.16.0.4 - - [29/Jun/2026:15:00:10 +0000] "POST /login HTTP/1.1" 403 120',

    ]
    with open("server_access.log", "w") as f:
        f.write("\n".join(sample_logs))

def analyze_logs(log_file_path):
        print(f"[*] Parsing log file:{log_file_path}")
        print("="*60)

        ip_counter = Counter()
        error_404_counter = Counter()
        timestamp_counter = defaultdict(list)

        log_pattern =  re.compile(
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?' #finds IP from regex
            r'\[(?P<timestamp>.*?)\] ".*?" ' #finds timestamp inside[]
            r'(?P<status>\d{3})'     #finds 3-digit status code
        )
        with open(log_file_path, "r" ) as f:
            for line in f:
                match = log_pattern.search(line)
                if match:
                    ip = match.group("ip")
                    timestamp_str = match.group("timestamp")
                    status = match.group("status")

                    ip_counter[ip] += 1

                    if status == "404":
                        error_404_counter[ip] += 1

                    time_second = timestamp_str.split(" ")[0]
                    timestamp_counter[ip].append(time_second)
        print("\n TOTAL REQUESTS PER IP:")
        for ip, count in ip_counter.most_common():
            print(f"  -> {ip:<15}:{count} requests")
        print("\n Detecting suspicious patterns:")

        for ip, count in error_404_counter.items():
            if count >= 3:
                print(f" SCANNER FLAG IP -- {ip} flagged for directory Brute-Forcing ({count} x 404 errors")
        for ip,times in timestamp_counter.items():
            time_counts = Counter(times)
            for sec, count in time_counts.items():
                if count >= 4:
                    print(f" FLOOD FLAG IP -- {ip} Flagged for High Speed Rate Abuse ({count} x 404 errors")
if __name__ == "__main__":
    generate_fake_logs()
    analyze_logs("Server_access.log")