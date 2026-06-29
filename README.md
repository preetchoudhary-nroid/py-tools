Py-Tools: 
---------
Project Dashboard
Tools
Core Technologies
1.Basic Vulnerability Scanner (v1)
-Sockets, Banner Grabbing, Signatures
2.Packet Sniffer, Netcat Clone
-Scapy, Raw Sockets, Multithreading
3.Subdomain Scanner, Network Info Scanner
-DNS Resolution, HTTP Headers, urllib
4.SSH Brute Forcer, Hash Cracker
-Paramiko, Hashlib, Wordlist Processing
5.Log Analyzer, Input Event Auditor
-Regular Expressions, pynput, File I/O
6.Automated File Organizer
-os, shutil, Transaction-Memory Logic
7.Caesar Cipher Engine
-ord/chr, Modular Arithmetic


1. Clone the Repository
Open your terminal and run:
git clone https://github.com/preetchoudhary-nroid/py-tools.git
cd py-tools
2. Install Required Libraries
These tools require third-party libraries to handle network packets, SSH protocols, and web requests
.
pip install scapy paramiko requests pynput
Note for Linux/Kali users: If your environment is externally managed, use --break-system-packages
.
3. Network Driver Requirement (Windows)
The Packet Sniffer requires the Npcap driver. During installation, you must check the box for "Install Npcap in WinPcap API-compatible Mode" to allow the Scapy library to interface with your network hardware
.

Basic Vulnerability Scanner (Version 1)
This tool performs service enumeration by initiating a TCP Three-Way Handshake (SYN -> SYN-ACK -> ACK)
. Once a live pipeline is opened, the engine utilizes Banner Grabbing via s.recv to extract service identity strings
. It cleans raw data using .decode(errors='ignore') to prevent crashes from proprietary binary data
. Finally, it normalizes the banner—stripping whitespace and forcing lowercase—to match it against a signature-based database of known vulnerable versions
.
Network Packet Sniffer
A "digital wiretap" that intercepts live traffic at the data-link layer using Scapy
. It parses IP Headers to extract source/destination addresses and identifies protocols like TCP, UDP, and ICMP
. The sniffer includes a Payload Preview engine that converts raw bytes into readable ASCII text, replacing non-printable characters with dots to ensure terminal stability
.
Custom Netcat Utility
A lightweight implementation of the classic Netcat tool for point-to-point communication
. It supports two modes:
Interactive Chat: Uses SOCK_STREAM for reliable TCP data transfer
.
Command Execution: Leverages the subprocess library to execute remote system commands and return the output (stdout/stderr) over the network
.
File Transfer: Implements a custom protocol that sends a Metadata Header (filename and size) before streaming raw bytes using binary chunking
.
SSH Service Auditor
Designed to audit authentication security on Port 22, this tool uses the Paramiko library to manage encrypted network channels
. It automates credential testing against a target host using high-speed wordlist attacks
. The engine is optimized for stability with an AutoAddPolicy for host keys and a 3-second timeout guard to prevent dead sockets from stalling the audit
.
Log Analyzer & Security Data Extractor
These tools utilize Regular Expressions (Regex) to perform "cookie-cutter" data isolation
.
Log Analysis: Scans Apache/Nginx logs to detect Directory Brute-Forcing (high frequency of 404 errors) and Rate Abuse (multiple requests per second)
.
Data Extraction: Uses patterns like \d{1,3}\.\d{1,3}... to automatically carve out IP addresses, emails, and URLs from messy, unstructured text files
.



Ethics and Disclaimer
FOR EDUCATIONAL AND DEFENSIVE AUDITING PURPOSES ONLY. The tools in this repository were developed to understand the mechanics of system vulnerabilities and endpoint defenses
. Unauthorized access to computer systems is illegal. All testing and development were performed strictly on self-owned virtual machines and local network environments
. Use these tools responsibly and only on systems where you have explicit permission to audit.
The owner of this repository accepts no responsibility and is not liable for any illegal activities, data loss, or system damages caused by the misuse of this code.
---
