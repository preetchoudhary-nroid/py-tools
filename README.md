# Py-Tools

A collection of Python-based cybersecurity tools covering network reconnaissance, vulnerability scanning, packet analysis, authentication auditing, and security data extraction. Built for hands-on offensive/defensive security learning.

⚠️ **Disclaimer:** These tools are built for educational purposes and authorized security testing only. Only use them against systems, networks, or accounts you own or have explicit written permission to test. Unauthorized use may be illegal.

---

## 🧰 Project Dashboard

| Tool | Core Technologies |
|---|---|
| Basic Vulnerability Scanner (v1) | Sockets, Banner Grabbing, Signatures |
| Packet Sniffer, Netcat Clone | Scapy, Raw Sockets, Multithreading |
| Subdomain Scanner, Network Info Scanner | DNS Resolution, HTTP Headers, urllib |
| SSH Brute Forcer, Hash Cracker | Paramiko, Hashlib, Wordlist Processing |
| Log Analyzer, Input Event Auditor | Regular Expressions, pynput, File I/O |
| Automated File Organizer | os, shutil, Transaction-Memory Logic |
| Caesar Cipher Engine | ord/chr, Modular Arithmetic |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/preetchoudhary-nroid/py-tools.git
cd py-tools
```

### 2. Install Required Libraries
These tools require third-party libraries to handle network packets, SSH protocols, and web requests.
```bash
pip install scapy paramiko requests pynput
```
**Note for Linux/Kali users:** If your environment is externally managed, use:
```bash
pip install scapy paramiko requests pynput --break-system-packages
```

### 3. Network Driver Requirement (Windows Only)
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

---

## Requirements

- Python 3.x
- `scapy`, `paramiko`, `requests`, `pynput`
- Npcap (Windows only, for packet sniffing)

## License

For educational use. Use responsibly and only on systems and networks you own or are explicitly authorized to test.
