# py-tools

A collection of foundational Python scripts built for network reconnaissance, system administration automation, and endpoint input auditing. This repository serves as a hands-on technical portfolio demonstrating socket programming, file-system interaction, and security analysis.

---

## Legal and Ethical Disclaimer

IMPORTANT: The tools contained within this repository are developed strictly for educational purposes, defensive analysis, and authorized penetration testing audits. 

* DO NOT execute any network scanning or monitoring tools against systems without explicit, written prior authorization from the system owner.
* The author accepts absolutely no liability and is not responsible for any misuse, damage, or illegal activity caused by these scripts. 

---

## Included Tools and Modules

### 1. Automated Port Scanner (port_scanner.py)
A network scouting utility that probes a range of target ports to map active services.
* Core Concepts: Sockets (connect_ex), input sanitization, error-handling overrides.
* Features: Maps ports to known common services (21=FTP, 22=SSH, 80=HTTP, 443=HTTPS) and generates an automated summary log file upon completion.

### 2. Maintenance File Organizer (file_organizer.py)
An automated system administrative script that scans cluttered directories and groups loose files cleanly by their extensions.
* Core Concepts: OS file-system manipulation (os), high-level file utilities (shutil).
* Features: Dynamic path isolation, directory mapping, and a structural transaction memory engine that allows users to seamlessly Undo and reverse the entire sorting operation.

### 3. Custom Netcat Utility (netcat_clone.py)
A lightweight, raw-socket implementation modeling the classic Netcat utility for point-to-point network communication.
* Core Concepts: TCP stream manipulation (SOCK_STREAM), data byte chunking (send/recv).
* Features: Supports interactive terminal chat streams and point-to-point file transfers between a local client and a listening server.

### 4. Input Event Auditor (keylogger.py)
An educational script designed to analyze how operating systems capture peripheral hardware inputs via low-level hooks.
* Core Concepts: Operating system event listeners, hardware hooks (pynput).
* Features: Distinguishes between textual alphanumeric inputs and special command keystrokes with event logging. Used to study how endpoint tracking occurs and how to build system-level defenses against spyware.

---

## Installation and Environment Setup

To run these tools locally, ensure you have Python 3 installed, clone the repository, and install the required peripheral tracking library.

```bash
# 1. Clone the repository
git clone [https://github.com/preetchoudhary-nroid/py-tools.git](https://github.com/preetchoudhary-nroid/py-tools.git)

# 2. Navigate into the project folder
cd py-tools

# 3. Install required hardware monitoring modules
pip install pynput
