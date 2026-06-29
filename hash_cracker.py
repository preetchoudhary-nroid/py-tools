#CRYPTOGRAPHIC HASH CRACKER
#hashlib will be used.
import hashlib
import time
def crack_hash(target_hash, hash_type):
    print(f"\n[+]Target Hash to Crack: {target_hash}")
    print(f"[*]Algorithm Selected:{hash_type.upper()} ")
    print("[*]Launching brute-Force dictionary attack...")
    print("="*60)
    wordlist = [
        "password", "123456", "qwerty", "admin123",
        "security", "blue-denim", "hunter2", "letmein123","admin"
    ]

    start_time = time.time()
    attempts = 0
    for word in wordlist:
        attempts += 1
        word_bytes = word.encode("utf-8")
        if hash_type.lower() == "md5":
            guess_hash = hashlib.md5(word_bytes).hexdigest()
        elif hash_type.lower() == "sha1":
            guess_hash = hashlib.sha1(word_bytes).hexdigest()
        else:
            print("[!]Unsupported hash Algorithm Type.")
            return
        if guess_hash == target_hash:
            duration = time.time() - start_time
            print(f"CRACKED!!! SUCCESS Match found after {attempts} attempts")
            print(f"  ->Plaintext Password: {word}")
            print(f"  ->Time Elapsed      : {duration:.4f} seconds")
            print("="*60)
            return
        print("="*60)
        print(f"FAILED - WORDLIST EXHAUSTED. Tested {attempts} words without a match.")
if __name__ == "__main__":
    print("===========================================")
    print("    CRYPTOGRAPHIC HASH CRACKING UTILITY    ")
    print("===========================================")

    stolen_hash_sample = input("\n[+]Enter the HASH:")
    hash_type = input("[+]Enter hash type md5 or sha1:").strip().lower()
    crack_hash(stolen_hash_sample, hash_type)
