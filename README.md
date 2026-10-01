# Py-Tools

A comprehensive collection of Python-based cybersecurity tools covering network reconnaissance, vulnerability scanning, packet analysis, authentication auditing, and security data extraction. Built for hands-on offensive/defensive security learning with both command-line and graphical user interface options.

⚠️ **Disclaimer:** These tools are built for educational purposes and authorized security testing only. Only use them against systems, networks, or accounts you own or have explicit written permission to test. Unauthorized use may be illegal.

---

## 🎯 New Feature: Security Tools UI Suite

**Graphical User Interface** now available! All cybersecurity tools have been integrated into a single, easy-to-use application with a tabbed interface.

### Quick Start with UI
```bash
cd security_tools_ui
pip install -r requirements.txt
python main.py
```

The UI includes 12 integrated tools:
- Password Generator, Caesar Cipher, File Organizer
- Hash Cracker, Port Scanner, Regex Extractor
- Log Analyzer, Subdomain Scanner, Uptime Checker
- Network Info Scanner, Directory Bruter, Vulnerability Scanner

---

## 🧰 Project Dashboard

| Tool | Core Technologies |
|---|---|
| **Security Tools UI Suite** | tkinter, Complete GUI Integration |
| Basic Vulnerability Scanner (v1) | Sockets, Banner Grabbing, Signatures |
| Packet Sniffer, Netcat Clone | Scapy, Raw Sockets, Multithreading |
| Subdomain Scanner, Network Info Scanner | DNS Resolution, HTTP Headers, urllib |
| SSH Brute Forcer, Hash Cracker | Paramiko, Hashlib, Wordlist Processing |
| Log Analyzer, Input Event Auditor | Regular Expressions, pynput, File I/O |
| Automated File Organizer | os, shutil, Transaction-Memory Logic |
| Caesar Cipher Engine | ord/chr, Modular Arithmetic |
| Password Generator | random, string, Strength Analysis |
| Port Scanner | socket, Service Enumeration |
| Regex Extractor | re, Pattern Matching |
| Directory Bruter | requests, Path Discovery |
| Uptime Checker | requests, HTTP Monitoring |
| Vulnerability Scanner | socket, Banner Analysis |

---

## 🚀 Getting Started

### Option 1: Using the Graphical User Interface (Recommended)

**For beginners and users who prefer a visual interface:**

```bash
git clone https://github.com/preetchoudhary-nroid/py-tools.git
cd py-tools/security_tools_ui
pip install -r requirements.txt
python main.py
```

The UI provides an intuitive tabbed interface with all 12 tools integrated into a single application. No command-line knowledge required!

### Option 2: Using Command-Line Tools

**For advanced users and automation:**

```bash
git clone https://github.com/preetchoudhary-nroid/py-tools.git
cd py-tools
```

#### Install Required Libraries
These tools require third-party libraries to handle network packets, SSH protocols, and web requests.
```bash
pip install scapy paramiko requests pynput
```
**Note for Linux/Kali users:** If your environment is externally managed, use:
```bash
pip install scapy paramiko requests pynput --break-system-packages
```

#### Network Driver Requirement (Windows Only)
The Packet Sniffer requires the **Npcap** driver. During installation, check the box for **"Install Npcap in WinPcap API-compatible Mode"** to allow Scapy to interface with your network hardware.

---

## 🔎 Basic Vulnerability Scanner (v1)

Performs service enumeration by initiating a TCP Three-Way Handshake (SYN → SYN-ACK → ACK). Once a live connection is opened, the engine performs **Banner Grabbing** via `s.recv` to extract service identity strings. Raw data is cleaned using `.decode(errors='ignore')` to prevent crashes from proprietary binary data, then normalized — stripped of whitespace and lowercased — to match against a signature-based database of known vulnerable versions.

---

## 📡 Network Packet Sniffer

A "digital wiretap" that intercepts live traffic at the data-link layer using **Scapy**. It parses IP headers to extract source/destination addresses and identifies protocols like TCP, UDP, and ICMP. Includes a **Payload Preview** engine that converts raw bytes into readable ASCII text, replacing non-printable characters with dots to keep terminal output stable.

---

## 💻 Custom Netcat Utility

A lightweight implementation of the classic Netcat tool for point-to-point communication. Supports three modes:

- **Interactive Chat** — Uses `SOCK_STREAM` for reliable TCP data transfer.
- **Command Execution** — Leverages the `subprocess` library to execute remote system commands and return output (stdout/stderr) over the network.
- **File Transfer** — Implements a custom protocol that sends a metadata header (filename and size) before streaming raw bytes using binary chunking.

---

## 🔐 SSH Service Auditor

Audits authentication security on Port 22 using the **Paramiko** library to manage encrypted network channels. Automates credential testing against a target host using high-speed wordlist attacks. Optimized for stability with an `AutoAddPolicy` for host keys and a 3-second timeout guard to prevent dead sockets from stalling the audit.

---

## 📋 Log Analyzer & Security Data Extractor

Uses **Regular Expressions** to perform targeted data isolation from logs and text:

- **Log Analysis** — Scans Apache/Nginx logs to detect directory brute-forcing (high frequency of 404 errors) and rate abuse (multiple requests per second).
- **Data Extraction** — Uses regex patterns to automatically carve out IP addresses, emails, and URLs from messy, unstructured text files.

---

## 🛠️ Other Tools

- **Subdomain Scanner / Network Info Scanner** — DNS resolution and HTTP header inspection to map network/domain information.
- **Hash Cracker** — Wordlist-based cracking using `hashlib`.
- **Automated File Organizer** — Sorts files using `os`/`shutil` with transaction-memory logic to safely track and reverse moves.
- **Caesar Cipher Engine** — Classic substitution cipher implementation using `ord`/`chr` and modular arithmetic.
- **Password Generator** — Creates secure passwords with customizable options and strength analysis.
- **Port Scanner** — Multi-port scanning with service identification and report generation.
- **Regex Extractor** — Extracts IP addresses, emails, and URLs from text files using pattern matching.
- **Directory Bruter** — Web path discovery tool for finding hidden directories and files.
- **Uptime Checker** — Website availability monitoring with HTTP status analysis.
- **Vulnerability Scanner** — Service banner analysis against known vulnerability database.

---

## 📚 Educational Resources

### Networking Basics Documentation
- **NETWORKING BASICS03.py** — Comprehensive guide covering TCP vs UDP protocols, 3-way handshake, and core service ports reference for security auditing.
- **NETWORKING BASICS04.py** — DNS system documentation including record types, security implications, and common attack vectors (DNS spoofing, cache poisoning, zone transfers).

These educational materials provide foundational knowledge for understanding the protocols and services that the security tools interact with.

---

## Requirements

### For UI Suite:
- Python 3.x
- `requests` (for web-based tools)
- `tkinter` (usually included with Python)

### For Command-Line Tools:
- Python 3.x
- `scapy`, `paramiko`, `requests`, `pynput`
- Npcap (Windows only, for packet sniffing)

## 📁 Project Structure

```
py-tools/
├── security_tools_ui/          # Graphical User Interface Suite
│   ├── main.py                # Main UI application
│   ├── requirements.txt       # UI dependencies
│   └── README.md              # UI-specific documentation
├── caesar_cipher.py           # Encryption/decryption tool
├── file_organizer.py          # Automated file sorting
├── hash_cracker.py            # Hash cracking utility
├── port_scanner.py            # Network port scanner
├── regex_extractor.py         # Data extraction tool
├── log_analyzer.py            # Security log analysis
├── subdomain_scanner.py       # DNS subdomain discovery
├── uptime_checker.py          # Website monitoring
├── network_info_scanner.py    # Network reconnaissance
├── dir_bruter.py              # Web directory brute-forcing
├── vulnerability_scanner.py   # Service vulnerability detection
├── NETWORKING BASICS03.py     # TCP/UDP protocol documentation
├── NETWORKING BASICS04.py     # DNS system documentation
└── README.md                  # This file
```

## 🤝 Contributing

Contributions are welcome! This project is designed for educational purposes and learning. Feel free to:
- Report bugs or issues
- Suggest new security tools
- Improve existing tool functionality
- Enhance documentation
- Add more educational resources

## 📖 Usage Examples

### UI Suite Example
```bash
cd security_tools_ui
python main.py
# Navigate through tabs to use different tools
# Example: Use Password Generator tab to create secure passwords
```

### Command-Line Example
```bash
# Port scanning
python port_scanner.py
# Enter target IP and port range when prompted

# Hash cracking
python hash_cracker.py
# Enter target hash and hash type (md5/sha1)

# Subdomain discovery
python subdomain_scanner.py
# Enter target domain (e.g., example.com)
```

## ⚠️ Legal and Ethical Guidelines

- **Authorization Only**: Use these tools only on systems you own or have explicit permission to test
- **Educational Purpose**: Designed for learning security concepts and authorized testing
- **Responsible Disclosure**: If you discover vulnerabilities, follow responsible disclosure practices
- **Legal Compliance**: Ensure compliance with local laws and regulations regarding security testing

## 📄 License

For educational use. Use responsibly and only on systems and networks you own or are explicitly authorized to test.

## 🔗 Resources

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Nmap Documentation](https://nmap.org/book/)
- [Python Security Documentation](https://docs.python.org/3/library/security.html)

---

**Built for cybersecurity education and responsible security testing.**
