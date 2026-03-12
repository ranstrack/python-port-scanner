# portscanner.py
import socket
import threading
import argparse

# Function to scan a single port
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Threaded scan function
def scan_ports(target, ports):
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# Main function to handle user input
def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("port_range", help="Port range, e.g., 20-1024")
    args = parser.parse_args()

    # Parse port range
    try:
        start_port, end_port = map(int, args.port_range.split('-'))
        ports = range(start_port, end_port + 1)
    except ValueError:
        print("Invalid port range format. Use start-end, e.g., 20-1024")
        return

    print(f"Scanning {args.target} ports {start_port}-{end_port}...\n")
    scan_ports(args.target, ports)
    print("\nScan completed!")

if __name__ == "__main__":
    main()