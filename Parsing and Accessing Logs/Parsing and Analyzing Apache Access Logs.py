#This code reads an Apache access log file, parses the log entries, and performs basic analysis, counting requests by IP address. 
#You can extend the analysis based on your specific requirements.

#Python Script for Parsing and Analyzing Apache Access Logs:

import re
from collections import Counter

def parse_apache_access_log(log_file):
    log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'
    log_entries = []

    with open(log_file, 'r') as file:
        for line in file:
            match = re.match(log_pattern, line)
            if match:
                ip_address = match.group(1)
                timestamp = match.group(2)
                request = match.group(3)
                status_code = match.group(4)
                user_agent = match.group(7)

                log_entry = {
                    'ip_address': ip_address,
                    'timestamp': timestamp,
                    'request': request,
                    'status_code': status_code,
                    'user_agent': user_agent,
                }
                log_entries.append(log_entry)

    return log_entries

def analyze_access_logs(log_entries):
    # Example analysis: Count requests by IP address
    ip_counter = Counter(entry['ip_address'] for entry in log_entries)
    most_common_ips = ip_counter.most_common(10)

    return most_common_ips

if __name__ == '__main__':
    log_file = 'path/to/apache/access.log'
    log_entries = parse_apache_access_log(log_file)
    most_common_ips = analyze_access_logs(log_entries)
    print("Most common IP addresses:")
    for ip, count in most_common_ips:
        print(f"{ip}: {count} requests")
