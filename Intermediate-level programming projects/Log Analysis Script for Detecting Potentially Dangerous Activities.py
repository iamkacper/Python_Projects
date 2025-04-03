""" A log analysis script is useful for security monitoring. It processes server logs (e.g., Apache, Nginx) and detects potentially dangerous activities, 
such as multiple failed login attempts, suspicious IP addresses, or other abnormal behavior that could indicate a security threat.

Basic Concept:
Input: Apache or Nginx server log files.

Output: Detected suspicious activities like repeated failed login attempts from a specific IP address or any other unusual activity.

We will use Python to create a simple script that can process these logs and detect multiple failed login attempts.

Sample Log Analysis Script
This script will:

Parse log files.

Detect repeated failed login attempts (e.g., from SSH, HTTP, or FTP).

Output suspicious IP addresses and alert for potential brute-force attacks. """

import re
from collections import defaultdict

# Define a function to process the logs
def analyze_logs(log_file, threshold=5):
    """
    Analyzes the server log for failed login attempts and detects suspicious IP addresses.
    
    Args:
    - log_file (str): Path to the log file to analyze.
    - threshold (int): Number of failed attempts from the same IP to trigger an alert.
    
    Returns:
    - Suspicious IP addresses with the number of failed login attempts.
    """
    # Dictionary to keep track of failed attempts per IP address
    failed_attempts = defaultdict(int)

    # Regular expression pattern to match failed login attempts
    # This pattern can be adjusted for different types of logs (e.g., Apache, Nginx, SSH)
    failed_login_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*\bfailed\b')

    # Open the log file and process each line
    with open(log_file, 'r') as file:
        for line in file:
            match = failed_login_pattern.search(line)
            if match:
                ip_address = match.group('ip')
                failed_attempts[ip_address] += 1

    # Print IP addresses with more than the threshold of failed attempts
    print(f"\nSuspicious IP addresses (more than {threshold} failed attempts):")
    for ip, count in failed_attempts.items():
        if count >= threshold:
            print(f"IP: {ip}, Failed Attempts: {count}")

# Main function
if __name__ == "__main__":
    log_file = input("Enter the log file path: ")
    threshold = int(input("Enter the threshold for failed attempts (default 5): ") or 5)
    analyze_logs(log_file, threshold)

""" 
Additional Features:
- Adjust Regex for Different Logs: The regular expression (failed_login_pattern) can be modified for various log formats. For example, for Nginx or SSH, the pattern can be changed to match lines that contain "Authentication failed" or similar terms.

- Output to File: You can modify the script to log suspicious IPs to a file for further investigation.

- Alerting System: For a more advanced system, you can integrate email or SMS alerts when suspicious activities are detected.

- Other Suspicious Activities: The script can be extended to check for other activities, such as too many connections from the same IP, suspicious user agents, or requests to restricted pages.

This script can be used as a simple, effective tool for monitoring security on servers and identifying potential brute-force attacks or other malicious activities. 
"""