""" Port Scanner in python
This script is used to scan open ports on a target system (IP address or domain). 
It uses the socket library to attempt connections to the ports and multi-threading to speed up the scanning process. 
The script checks ports within a specified range and informs you which ports are open and which are closed. """

""" Use this script only on systems you are authorized to scan to avoid legal issues! """

import socket
import threading
from datetime import datetime

# AES block size (16 bytes for AES)
BLOCK_SIZE = 16

# Global list to hold open ports
open_ports = []

# Function to scan a single port
def scan_port(target, port, timeout=1):
    """Try to connect to a given port on the target and check if it's open."""
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set timeout for connection attempt
            s.settimeout(timeout)
            # Attempt to connect to the target and port
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
    except socket.error as err:
        print(f"Error scanning port {port}: {err}")

# Function to scan a range of ports concurrently using threading
def scan_ports_concurrently(target, start_port, end_port, timeout=1):
    """Scan a range of ports on the target using threads."""
    print(f"Scanning target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}")
    print("-" * 50)

    start_time = datetime.now()
    threads = []

    # Create and start a new thread for each port
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, timeout))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = datetime.now()
    print("-" * 50)
    print(f"Scan completed in {end_time - start_time}")
    print(f"Open ports: {open_ports}")

# Main program
if __name__ == "__main__":
    target = input("Enter the target IP address or domain: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    timeout = float(input("Enter the timeout duration (in seconds, e.g., 1): "))

    scan_ports_concurrently(target, start_port, end_port, timeout)