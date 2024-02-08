import ssl
import socket
from datetime import datetime
import argparse
import certifi
import tabulate

def parse_arguments():
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description='Check SSL certificate expiration for a list of domains.')
    parser.add_argument('file_path', type=str, help='Path to the file containing domain names.')
    return parser.parse_args()

# Function which parses a file with domains and returns a list of domains
def get_domains_from_file(file_path):
    """Parse a file with domain names and return a list of domains."""

    with open(file_path, "r") as file:
        return file.read().splitlines()

def check_ssl_expiry(domain):
    """Check the SSL certificate expiration for a domain."""

    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context(cafile=certifi.where())

    try:
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=domain,
        )
        # 3 second timeout to ensure the script doesn't hang
        conn.settimeout(3.0)
        
        conn.connect((domain, 443))
        ssl_info = conn.getpeercert()
        # Parse the string from the certificate into a Python datetime object
        expires = datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        days_remaining = (expires - datetime.now()).days
        return days_remaining
    except Exception as e:
        return str(e)  # Return error message as a string

def ssl_report(domains):
    """Generate a report on SSL certificate expiration for a list of domains."""

    headers = ['Domain', 'Status', 'Days Remaining/Overdue']
    report_data = []
    for domain in domains:
        result = check_ssl_expiry(domain)
        if isinstance(result, int):
            status = "Valid" if result > 0 else "Expired"
            report_data.append([domain, status, result])
        else:
            report_data.append([domain, "SSL check failed", result])
    return { "headers": headers, "data": report_data}

def main():
    """Main function."""
    # Parse command line arguments
    args = parse_arguments()
    file_path = args.file_path

    # Get domains from file and generate report
    domains = get_domains_from_file(file_path)
    report = ssl_report(domains)

    # if second column is not integer, replace it with -1
    for row in report['data']:
        if not isinstance(row[2], int):
            row[2] = -99999
    # sort by days remaining
    report['data'].sort(key=lambda x: x[2])
    print(tabulate.tabulate(report['data'], headers=report['headers'], tablefmt="grid"))

if __name__ == "__main__":
    main()
