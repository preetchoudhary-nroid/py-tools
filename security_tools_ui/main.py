import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import random
import string
import hashlib
import time
import socket
import re
import os
import shutil
import requests
from datetime import datetime
from collections import Counter, defaultdict
import threading


class SecurityToolsUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Tools Suite")
        self.root.geometry("1000x700")
        
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs for each tool
        self.create_password_generator_tab()
        self.create_caesar_cipher_tab()
        self.create_file_organizer_tab()
        self.create_hash_cracker_tab()
        self.create_port_scanner_tab()
        self.create_regex_extractor_tab()
        self.create_log_analyzer_tab()
        self.create_subdomain_scanner_tab()
        self.create_uptime_checker_tab()
        self.create_network_info_scanner_tab()
        self.create_directory_bruter_tab()
        self.create_vulnerability_scanner_tab()
        
    def create_password_generator_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Password Generator")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Password Generator", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Length input
        ttk.Label(frame, text="Length:").pack(anchor='w')
        self.pass_length = ttk.Entry(frame)
        self.pass_length.insert(0, "12")
        self.pass_length.pack(fill='x', pady=5)
        
        # Checkboxes
        self.pass_upper = tk.BooleanVar(value=True)
        self.pass_digits = tk.BooleanVar(value=True)
        self.pass_symbols = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(frame, text="Include Uppercase", variable=self.pass_upper).pack(anchor='w')
        ttk.Checkbutton(frame, text="Include Digits", variable=self.pass_digits).pack(anchor='w')
        ttk.Checkbutton(frame, text="Include Symbols", variable=self.pass_symbols).pack(anchor='w')
        
        ttk.Button(frame, text="Generate Password", command=self.generate_password).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Generated Password:").pack(anchor='w', pady=(10, 0))
        self.pass_result = ttk.Entry(frame)
        self.pass_result.pack(fill='x', pady=5)
        
        ttk.Label(frame, text="Strength:").pack(anchor='w')
        self.pass_strength = ttk.Label(frame, text="")
        self.pass_strength.pack(anchor='w')
        
    def generate_password(self):
        try:
            length = int(self.pass_length.get())
            use_upper = self.pass_upper.get()
            use_digits = self.pass_digits.get()
            use_symbols = self.pass_symbols.get()
            
            chars = string.ascii_lowercase
            if use_upper:
                chars += string.ascii_uppercase
            if use_digits:
                chars += string.digits
            if use_symbols:
                chars += string.punctuation
            
            score = 1
            if use_upper: score += 1
            if use_digits: score += 1
            if use_symbols: score += 1
            
            if length >= 12 and score == 4:
                strength = "Strong"
            elif length >= 8 and score == 3:
                strength = "Medium"
            else:
                strength = "Weak"
            
            password = ''.join(random.choice(chars) for _ in range(length))
            self.pass_result.delete(0, tk.END)
            self.pass_result.insert(0, password)
            self.pass_strength.config(text=strength)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for length")
    
    def create_caesar_cipher_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Caesar Cipher")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Caesar Cipher Engine", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Operation selection
        ttk.Label(frame, text="Operation:").pack(anchor='w')
        self.cipher_operation = ttk.Combobox(frame, values=["Encrypt", "Decrypt", "Brute Force"])
        self.cipher_operation.current(0)
        self.cipher_operation.pack(fill='x', pady=5)
        
        # Text input
        ttk.Label(frame, text="Text:").pack(anchor='w')
        self.cipher_text = ttk.Entry(frame)
        self.cipher_text.pack(fill='x', pady=5)
        
        # Shift input
        ttk.Label(frame, text="Shift Number:").pack(anchor='w')
        self.cipher_shift = ttk.Entry(frame)
        self.cipher_shift.insert(0, "3")
        self.cipher_shift.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Process", command=self.process_cipher).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Result:").pack(anchor='w', pady=(10, 0))
        self.cipher_result = scrolledtext.ScrolledText(frame, height=10, width=50)
        self.cipher_result.pack(fill='both', expand=True, pady=5)
        
    def process_cipher(self):
        operation = self.cipher_operation.get()
        text = self.cipher_text.get()
        
        if operation == "Brute Force":
            result = ""
            for shift in range(1, 26):
                decrypted = ""
                for char in text:
                    if char.islower():
                        new_char = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
                        decrypted += new_char
                    elif char.isupper():
                        new_char = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
                        decrypted += new_char
                    else:
                        decrypted += char
                result += f"Key {shift:02d}: {decrypted}\n"
        else:
            try:
                shift = int(self.cipher_shift.get())
                if operation == "Decrypt":
                    shift = -shift
                
                result = ""
                for char in text:
                    if char.islower():
                        new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
                        result += new_char
                    elif char.isupper():
                        new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
                        result += new_char
                    else:
                        result += char
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid shift number")
                return
        
        self.cipher_result.delete(1.0, tk.END)
        self.cipher_result.insert(tk.END, result)
    
    def create_file_organizer_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="File Organizer")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Automated File Organizer", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Directory selection
        ttk.Label(frame, text="Target Directory:").pack(anchor='w')
        self.org_dir = ttk.Entry(frame)
        self.org_dir.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Browse", command=self.browse_directory).pack(anchor='w', pady=5)
        
        ttk.Button(frame, text="Organize Files", command=self.organize_files).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Results:").pack(anchor='w', pady=(10, 0))
        self.org_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.org_result.pack(fill='both', expand=True, pady=5)
        
        self.moved_files_history = []
        
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.org_dir.delete(0, tk.END)
            self.org_dir.insert(0, directory)
    
    def organize_files(self):
        target_dir = self.org_dir.get()
        if not target_dir or not os.path.exists(target_dir):
            messagebox.showerror("Error", "Please select a valid directory")
            return
        
        EXTENSION_MAP = {
            '.pdf': 'PDFs',
            '.docx': 'Documents',
            '.txt': 'Documents',
            '.jpg': 'Images',
            '.png': 'Images',
            '.mp4': 'Videos',
            '.zip': 'Archives'
        }
        
        files_moved_count = 0
        folders_created = set()
        self.moved_files_history = []
        
        result = f"[+] Scanning directory: {target_dir}\n\n"
        
        for filename in os.listdir(target_dir):
            source_path = os.path.join(target_dir, filename)
            
            if os.path.isdir(source_path):
                continue
            
            name, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            if ext in EXTENSION_MAP:
                subfolder_name = EXTENSION_MAP[ext]
                subfolder_path = os.path.join(target_dir, subfolder_name)
                
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)
                    folders_created.add(subfolder_name)
                
                destination_path = os.path.join(subfolder_path, filename)
                shutil.move(source_path, destination_path)
                
                self.moved_files_history.append((source_path, destination_path))
                files_moved_count += 1
                result += f"[->] Moved: {filename} to {subfolder_name}\n"
        
        result += "\n" + "="*40 + "\n"
        result += "SCAN SUMMARY\n"
        result += "="*40 + "\n"
        result += f"Total files moved: {files_moved_count}\n"
        result += f"Subfolders created: {len(folders_created)} ({','.join(folders_created) if folders_created else 'None'})\n"
        
        self.org_result.delete(1.0, tk.END)
        self.org_result.insert(tk.END, result)
        
        if files_moved_count > 0:
            if messagebox.askyesno("Undo", "Would you like to undo this operation?"):
                self.undo_file_organizer()
    
    def undo_file_organizer(self):
        for original_path, new_path in self.moved_files_history:
            if os.path.exists(new_path):
                shutil.move(new_path, original_path)
        
        self.org_result.delete(1.0, tk.END)
        self.org_result.insert(tk.END, "[+] UNDO OPERATION COMPLETE. ALL FILES RESTORED.\n")
    
    def create_hash_cracker_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Hash Cracker")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Cryptographic Hash Cracker", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Hash input
        ttk.Label(frame, text="Target Hash:").pack(anchor='w')
        self.hash_target = ttk.Entry(frame)
        self.hash_target.pack(fill='x', pady=5)
        
        # Hash type
        ttk.Label(frame, text="Hash Type:").pack(anchor='w')
        self.hash_type = ttk.Combobox(frame, values=["md5", "sha1"])
        self.hash_type.current(0)
        self.hash_type.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Crack Hash", command=self.crack_hash).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Results:").pack(anchor='w', pady=(10, 0))
        self.hash_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.hash_result.pack(fill='both', expand=True, pady=5)
        
    def crack_hash(self):
        target_hash = self.hash_target.get()
        hash_type = self.hash_type.get()
        
        wordlist = [
            "password", "123456", "qwerty", "admin123",
            "security", "blue-denim", "hunter2", "letmein123", "admin"
        ]
        
        result = f"[+] Target Hash: {target_hash}\n"
        result += f"[*] Algorithm: {hash_type.upper()}\n"
        result += "[*] Launching brute-force dictionary attack...\n"
        result += "="*60 + "\n"
        
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
                result += "[!] Unsupported hash algorithm\n"
                break
            
            if guess_hash == target_hash:
                duration = time.time() - start_time
                result += f"CRACKED!!! Match found after {attempts} attempts\n"
                result += f"  -> Plaintext: {word}\n"
                result += f"  -> Time: {duration:.4f} seconds\n"
                result += "="*60 + "\n"
                self.hash_result.delete(1.0, tk.END)
                self.hash_result.insert(tk.END, result)
                return
        
        result += "="*60 + "\n"
        result += f"FAILED - Wordlist exhausted. Tested {attempts} words without match.\n"
        self.hash_result.delete(1.0, tk.END)
        self.hash_result.insert(tk.END, result)
    
    def create_port_scanner_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Port Scanner")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Cybersecurity Automated Port Scanner", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Target IP
        ttk.Label(frame, text="Target IP:").pack(anchor='w')
        self.scan_ip = ttk.Entry(frame)
        self.scan_ip.pack(fill='x', pady=5)
        
        # Port range
        ttk.Label(frame, text="Start Port:").pack(anchor='w')
        self.scan_start = ttk.Entry(frame)
        self.scan_start.insert(0, "1")
        self.scan_start.pack(fill='x', pady=5)
        
        ttk.Label(frame, text="End Port:").pack(anchor='w')
        self.scan_end = ttk.Entry(frame)
        self.scan_end.insert(0, "1024")
        self.scan_end.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Start Scan", command=self.start_port_scan).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Scan Results:").pack(anchor='w', pady=(10, 0))
        self.scan_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.scan_result.pack(fill='both', expand=True, pady=5)
        
    def start_port_scan(self):
        target_ip = self.scan_ip.get()
        try:
            start_port = int(self.scan_start.get())
            end_port = int(self.scan_end.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid port numbers")
            return
        
        services = {
            21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS"
        }
        
        result = f"[!] Initializing scan on target: {target_ip}\n"
        result += "-"*50 + "\n"
        
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            
            try:
                scan_result = s.connect_ex((target_ip, port))
                
                if scan_result == 0:
                    service_name = services.get(port, "Unknown service")
                    result += f"[+] Port {port:<5} | STATUS: OPEN | SERVICE: {service_name}\n"
                else:
                    result += f"[-] Port {port:<5} | STATUS: CLOSED\n"
            except Exception as e:
                result += f"[-] Error scanning port {port:<5} | ERROR: {e}\n"
            finally:
                s.close()
        
        result += "-"*50 + "\n"
        result += "SCAN SUCCESSFULLY TERMINATED\n"
        
        self.scan_result.delete(1.0, tk.END)
        self.scan_result.insert(tk.END, result)
    
    def create_regex_extractor_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Regex Extractor")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Regex Security Data Extraction", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # File selection
        ttk.Label(frame, text="Select File:").pack(anchor='w')
        self.regex_file = ttk.Entry(frame)
        self.regex_file.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Browse", command=self.browse_regex_file).pack(anchor='w', pady=5)
        
        ttk.Button(frame, text="Extract Data", command=self.extract_regex_data).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Extracted Data:").pack(anchor='w', pady=(10, 0))
        self.regex_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.regex_result.pack(fill='both', expand=True, pady=5)
        
    def browse_regex_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            self.regex_file.delete(0, tk.END)
            self.regex_file.insert(0, filepath)
    
    def extract_regex_data(self):
        filepath = self.regex_file.get()
        if not filepath or not os.path.exists(filepath):
            messagebox.showerror("Error", "Please select a valid file")
            return
        
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file: {e}")
            return
        
        ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        email_pattern = r"[\w\.-]+@[\w\.-]+[a-zA-Z]{2,4}"
        url_pattern = r"https?://[^\s]+"
        
        extracted_ips = re.findall(ip_pattern, content)
        extracted_emails = re.findall(email_pattern, content)
        extracted_urls = re.findall(url_pattern, content)
        
        result = "="*50 + "\n"
        result += "REGEX SECURITY DATA EXTRACTION\n"
        result += "="*50 + "\n\n"
        
        result += "[+] Extracted IP ADDRESSES:\n"
        for ip in extracted_ips:
            result += f" ---{ip}\n"
        
        result += "\n[+] Extracted Email ADDRESSES:\n"
        for email in extracted_emails:
            result += f" ---{email}\n"
        
        result += "\n[+] Extracted URL ADDRESSES:\n"
        for url in extracted_urls:
            result += f" ---{url}\n"
        
        result += "="*50 + "\n"
        
        self.regex_result.delete(1.0, tk.END)
        self.regex_result.insert(tk.END, result)
    
    def create_log_analyzer_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Log Analyzer")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Security Log Analyzer", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # File selection
        ttk.Label(frame, text="Log File:").pack(anchor='w')
        self.log_file = ttk.Entry(frame)
        self.log_file.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Browse", command=self.browse_log_file).pack(anchor='w', pady=5)
        
        ttk.Button(frame, text="Analyze Logs", command=self.analyze_logs).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Analysis Results:").pack(anchor='w', pady=(10, 0))
        self.log_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.log_result.pack(fill='both', expand=True, pady=5)
        
    def browse_log_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Log files", "*.log"), ("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            self.log_file.delete(0, tk.END)
            self.log_file.insert(0, filepath)
    
    def analyze_logs(self):
        filepath = self.log_file.get()
        if not filepath or not os.path.exists(filepath):
            messagebox.showerror("Error", "Please select a valid log file")
            return
        
        result = f"[*] Parsing log file: {filepath}\n"
        result += "="*60 + "\n"
        
        ip_counter = Counter()
        error_404_counter = Counter()
        timestamp_counter = defaultdict(list)
        
        log_pattern = re.compile(
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?'
            r'\[(?P<timestamp>.*?)\] ".*?" '
            r'(?P<status>\d{3})'
        )
        
        try:
            with open(filepath, "r") as f:
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
        except Exception as e:
            messagebox.showerror("Error", f"Could not read log file: {e}")
            return
        
        result += "\nTOTAL REQUESTS PER IP:\n"
        for ip, count in ip_counter.most_common():
            result += f"  -> {ip:<15}: {count} requests\n"
        
        result += "\nDetecting suspicious patterns:\n"
        
        for ip, count in error_404_counter.items():
            if count >= 3:
                result += f" SCANNER FLAG IP -- {ip} flagged for directory brute-forcing ({count} x 404 errors)\n"
        
        for ip, times in timestamp_counter.items():
            time_counts = Counter(times)
            for sec, count in time_counts.items():
                if count >= 4:
                    result += f" FLOOD FLAG IP -- {ip} flagged for high-speed rate abuse ({count} requests)\n"
        
        self.log_result.delete(1.0, tk.END)
        self.log_result.insert(tk.END, result)
    
    def create_subdomain_scanner_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Subdomain Scanner")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Subdomain Discovery Engine", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Domain input
        ttk.Label(frame, text="Target Domain:").pack(anchor='w')
        self.subdomain_target = ttk.Entry(frame)
        self.subdomain_target.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Scan Subdomains", command=self.scan_subdomains).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Scan Results:").pack(anchor='w', pady=(10, 0))
        self.subdomain_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.subdomain_result.pack(fill='both', expand=True, pady=5)
        
    def scan_subdomains(self):
        target_domain = self.subdomain_target.get()
        if not target_domain:
            messagebox.showerror("Error", "Please enter a target domain")
            return
        
        result = f"[*] Target Domain: {target_domain}\n"
        result += "[*] Initializing DNS Discovery Engine...\n"
        result += "="*50 + "\n"
        
        subdomain_wordlist = [
            "www", "mail", "ftp", "admin", "dev", "test",
            "api", "vpn", "blog", "shop", "status", "support"
        ]
        
        found_count = 0
        start_time = time.time()
        
        for sub in subdomain_wordlist:
            full_host = f"{sub}.{target_domain}"
            
            try:
                ip_address = socket.gethostbyname(full_host)
                result += f"DISCOVERED -- {full_host:<25} | IP: {ip_address:<25}\n"
                found_count += 1
            except socket.gaierror:
                result += "HOST NOT FOUND\n"
                continue
        
        duration = time.time() - start_time
        result += "="*60 + "\n"
        result += f"[+] Scan completed. Found {found_count} active subdomains in {duration:.4f} seconds\n"
        
        self.subdomain_result.delete(1.0, tk.END)
        self.subdomain_result.insert(tk.END, result)
    
    def create_uptime_checker_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Uptime Checker")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Website Uptime Monitor", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # URL input
        ttk.Label(frame, text="Target URLs (one per line):").pack(anchor='w')
        self.uptime_urls = scrolledtext.ScrolledText(frame, height=5, width=50)
        self.uptime_urls.pack(fill='x', pady=5)
        self.uptime_urls.insert(tk.END, "https://www.google.com\nhttps://www.github.com")
        
        ttk.Button(frame, text="Check Uptime", command=self.check_uptime).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Results:").pack(anchor='w', pady=(10, 0))
        self.uptime_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.uptime_result.pack(fill='both', expand=True, pady=5)
        
    def check_uptime(self):
        urls_text = self.uptime_urls.get(1.0, tk.END).strip()
        urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
        
        if not urls:
            messagebox.showerror("Error", "Please enter at least one URL")
            return
        
        result = f"[+] Running uptime audit at {time.strftime('%Y-%m-%d %H-%M-%S')}...\n"
        result += "="*50 + "\n"
        
        for url in urls:
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
                
                result += f"[{status_label}] {url}\n"
                result += f"     - Content type: {response.headers.get('Content-Type', 'Unknown')}\n"
                result += f"     - Server: {response.headers.get('server', 'Hidden/Protected')}\n"
            except requests.exceptions.Timeout:
                result += f"[-] TIMEOUT {url} - Took too long to respond\n"
            except requests.exceptions.ConnectionError:
                result += f"[-] OFFLINE {url} - UNREACHABLE\n"
            except Exception as e:
                result += f"[-] ERROR {url}: {e}\n"
        
        result += "="*50 + "\n"
        
        self.uptime_result.delete(1.0, tk.END)
        self.uptime_result.insert(tk.END, result)
    
    def create_network_info_scanner_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Network Info Scanner")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Network Information Scanner", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Domain input
        ttk.Label(frame, text="Target Domain:").pack(anchor='w')
        self.netinfo_domain = ttk.Entry(frame)
        self.netinfo_domain.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Scan Network Info", command=self.scan_network_info).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Scan Results:").pack(anchor='w', pady=(10, 0))
        self.netinfo_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.netinfo_result.pack(fill='both', expand=True, pady=5)
        
    def scan_network_info(self):
        domain = self.netinfo_domain.get()
        if not domain:
            messagebox.showerror("Error", "Please enter a target domain")
            return
        
        result = f"[*] Resolving DNS for {domain}\n"
        
        ip_address = None
        reverse_hostname = None
        headers = {}
        open_ports = []
        
        try:
            ip_address = socket.gethostbyname(domain)
            result += f"[+] IP Address: {ip_address}\n"
            
            try:
                reverse_hostname = socket.gethostbyaddr(domain)
                result += f"[+] Reverse Hostname: {reverse_hostname}\n"
            except socket.herror:
                result += "[!] Reverse DNS failed\n"
        except socket.gaierror:
            result += f"[!] Error: Could NOT resolve {domain}\n"
            self.netinfo_result.delete(1.0, tk.END)
            self.netinfo_result.insert(tk.END, result)
            return
        
        # Scan common ports
        result += "\n[*] Testing web server ports...\n"
        ports_to_test = [80, 443]
        
        for port in ports_to_test:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2.0)
            scan_result = s.connect_ex((ip_address, port))
            if scan_result == 0:
                open_ports.append(port)
                result += f"[+] Port {port}: OPEN\n"
            else:
                result += f"[-] Port {port}: CLOSED\n"
            s.close()
        
        # Try to get HTTP headers
        result += "\n[*] Fetching HTTP headers...\n"
        try:
            import urllib.request
            url = f"http://{domain}"
            req = urllib.request.Request(url, headers={'USER-AGENT': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                for key, value in response.getheaders():
                    headers[key] = value
                    if key.lower() in ['server', 'date', 'content-type', 'connection']:
                        result += f"  - {key}: {value}\n"
        except Exception as e:
            result += f"[!] Could not fetch headers: {e}\n"
        
        result += "\n" + "="*50 + "\n"
        
        self.netinfo_result.delete(1.0, tk.END)
        self.netinfo_result.insert(tk.END, result)
    
    def create_directory_bruter_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Directory Bruter")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Web Path Discovery Utility", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # URL input
        ttk.Label(frame, text="Target URL:").pack(anchor='w')
        self.dirbrute_url = ttk.Entry(frame)
        self.dirbrute_url.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Brute Force Directories", command=self.brute_force_dirs).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Scan Results:").pack(anchor='w', pady=(10, 0))
        self.dirbrute_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.dirbrute_result.pack(fill='both', expand=True, pady=5)
        
    def brute_force_dirs(self):
        target_url = self.dirbrute_url.get()
        if not target_url:
            messagebox.showerror("Error", "Please enter a target URL")
            return
        
        if not target_url.endswith("/"):
            target_url += "/"
        
        result = f"[*] Target URL: {target_url}\n"
        result += "[+] Loading path discovery engine...\n"
        result += "="*50 + "\n"
        
        wordlist = [
            "admin", "login", "dashboard", "api", "config",
            "backup", "secret", "images", "robots.txt", "phpinfo.php"
        ]
        
        found_count = 0
        
        for path in wordlist:
            full_url = f"{target_url}{path}"
            try:
                response = requests.get(full_url, timeout=3, headers={"User-Agent": "SecurityAudioBot/1.0"})
                
                if response.status_code == 200:
                    result += f"FOUND - 200 OK ---> {full_url}\n"
                    found_count += 1
                elif response.status_code in [301, 302]:
                    result += f"REDIRECT - {response.status_code} ---> {full_url}\n"
                    found_count += 1
                elif response.status_code == 403:
                    result += f"FORBIDDEN - 403 ---> {full_url} (Directory exists but restricted)\n"
                    found_count += 1
            except requests.exceptions.RequestException as e:
                result += f"[-] ERROR ON {full_url}: {e}\n"
                continue
        
        result += "="*60 + "\n"
        result += f"[+] Scan completed. Identified {found_count} active paths.\n"
        
        self.dirbrute_result.delete(1.0, tk.END)
        self.dirbrute_result.insert(tk.END, result)
    
    def create_vulnerability_scanner_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Vulnerability Scanner")
        
        frame = ttk.Frame(tab, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Vulnerability Scanner", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Target IP
        ttk.Label(frame, text="Target IP:").pack(anchor='w')
        self.vuln_ip = ttk.Entry(frame)
        self.vuln_ip.pack(fill='x', pady=5)
        
        # Ports
        ttk.Label(frame, text="Ports (comma separated):").pack(anchor='w')
        self.vuln_ports = ttk.Entry(frame)
        self.vuln_ports.insert(0, "21,22,80,443")
        self.vuln_ports.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Scan for Vulnerabilities", command=self.scan_vulnerabilities).pack(pady=10)
        
        # Result
        ttk.Label(frame, text="Scan Results:").pack(anchor='w', pady=(10, 0))
        self.vuln_result = scrolledtext.ScrolledText(frame, height=15, width=50)
        self.vuln_result.pack(fill='both', expand=True, pady=5)
        
    def scan_vulnerabilities(self):
        target_ip = self.vuln_ip.get()
        ports_str = self.vuln_ports.get()
        
        if not target_ip:
            messagebox.showerror("Error", "Please enter a target IP")
            return
        
        try:
            target_ports = [int(p.strip()) for p in ports_str.split(',')]
        except ValueError:
            messagebox.showerror("Error", "Please enter valid port numbers")
            return
        
        VULN_DATABASE = {
            "vsftpd 2.3.4": "CVE-2011-2523 - Backdoor Execution (High Risk)",
            "openssh 7.4p1": "Potential Information Disclosure (Medium Risk)",
            "apache 2.4.49": "CVE-2021-41773 - Path Traversal (Critical)",
            "log4j-core 2.14": "CVE-2021-44228 - Log4Shell RCE (Critical)"
        }
        
        result = "="*50 + "\n"
        result += "VULNERABILITY SCANNER\n"
        result += "="*50 + "\n"
        result += f"[*] Starting scan on {target_ip}\n\n"
        
        for port in target_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2.0)
            
            try:
                s.connect((target_ip, port))
                result += f"[+] Port: {port}\n"
                
                banner_raw = s.recv(1024)
                banner = banner_raw.decode(errors="ignore")
                result += f"[+] BANNER: {banner.strip()}\n"
                
                clean_banner = banner.strip().lower()
                vuln_found = False
                
                for signature, advisory in VULN_DATABASE.items():
                    if signature in clean_banner:
                        result += f"[!!!] VULNERABILITY IDENTIFIED: {advisory}\n"
                        vuln_found = True
                
                if not vuln_found:
                    result += "[-] No signature found in banner\n"
                
            except socket.timeout:
                result += f"[-] Timed out on port {port}\n"
            except Exception as e:
                result += f"[-] Error on port {port}: {e}\n"
            finally:
                s.close()
        
        result += "\nSCAN COMPLETE\n"
        
        self.vuln_result.delete(1.0, tk.END)
        self.vuln_result.insert(tk.END, result)


if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityToolsUI(root)
    root.mainloop()
