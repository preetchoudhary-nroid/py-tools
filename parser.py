import re
import time
import os

LOG_FILE = "/var/log/auth.log"
FAILED_THRESHOLD = 10
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
def generate_report(failed_dict):
      print("\n"+"="*50)
      print("             SECURITY AUDIT REPORT")
      print("="*50)
      print(f"{'IP ADDRESS' :<20} | {'FAILED ATTEMPTS':<15}")
      print("-"*50)

      for ip, count in failed_dict.items():
           status = "FLAG: ATTACKER" if count > FAILED_THRESHOLD else "[SAFE]"
           print(f"{ip:<20} | {count:<15} {status}")
      print("="*50 + "\n")
def monitor_auth_log():
    failed_attempts = {}
    print(f"Monitoring {LOG_FILE} continuously...")

    if not os.path.exists(LOG_FILE):
        print(f"ERROR: {LOG_FILE} not found.")
        return
    try:
       with open(LOG_FILE, "r") as f:
            f.seek(0,2)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(1)
                    continue
                if "Failed password" in line:
                    match = re.search(ip_pattern, line)
                    if match:
                        ip = match.group()
                        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

                        if failed_attempts[ip] == FAILED_THRESHOLD:
                           print(f"ALERT: IP {ip} flagged for 10+ failed attempts")
                           generate_report(failed_attempts)
    except KeyboardInterrupt:
        print("\n Auditing stopped. Final Report:")
        generate_report(failed_attempts)
    except PermissionError:
        print("ERROR: Permission Denied. Run with sudo.")
if __name__ == "__main__":
     monitor_auth_log()