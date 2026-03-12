# Python Port Scanner

A simple Python tool to scan a target host for open TCP ports.  
Useful for learning networking and basic pentesting.

## Features
- Scan a range of ports on any host
- Multi-threaded for faster scanning
- Simple, beginner-friendly Python code

## Installation
1. Make sure Python 3 is installed on your system.
2. (Optional) Install dependencies:
```bash
pip install -r requirements.txt
Usage
python portscanner.py <target> <port-range>
Examples:

Scan localhost ports 1-1024:

python portscanner.py 127.0.0.1 1-1024

Scan a remote host ports 20-100:

python portscanner.py 192.168.1.10 20-100
Output

Displays open ports in the terminal

Example:

[+] Port 22 is open
[+] Port 80 is open
Disclaimer

Use this tool only on networks you own or have permission to scan. Unauthorized scanning is illegal and unethical.

License

MIT License