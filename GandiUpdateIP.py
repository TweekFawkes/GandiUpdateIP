import os
import sys
import requests
from dotenv import dotenv_values
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

# Initialize colorama
init(strip=not sys.stdout.isatty())

def display_ascii_art():
    """Display cool ASCII art when the script runs."""
    cprint(figlet_format('GandiUpdateIP', font='slant'),
           'cyan', attrs=['bold'])

def get_current_ip():
    """Get the current IP address of the user."""
    try:
        response = requests.get("https://ipcurl.net/n", verify=False)
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error getting IP address: {e}")
        sys.exit(1)

def load_credentials(script_name):
    """Load credentials from the config file."""
    config_file = f"{os.path.splitext(script_name)[0]}.config"
    return dotenv_values(config_file)

def test_api_key(api_key):
    """Test if the API key is valid."""
    url = "https://api.gandi.net/v5/livedns/domains"
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Error testing API key: {e}")
        if response.status_code == 401:
            print("The API key is invalid or has expired.")
        elif response.status_code == 403:
            print("The API key doesn't have the necessary permissions.")
        return False

def get_all_records(domain, api_key):
    """Get all DNS records for the domain."""
    url = f"https://api.gandi.net/v5/livedns/domains/{domain}/records"
    headers = {"Authorization": f"Bearer {api_key}"}
    # Authorization: Bearer 

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error getting DNS records: {e}")
        print(f"Response content: {response.text}")
        sys.exit(1)

def update_dns_record(domain, subdomain, new_ip, api_key):
    """Update the DNS A record for the given domain and subdomain."""
    url = f"https://api.gandi.net/v5/livedns/domains/{domain}/records/{subdomain}/A"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "rrset_values": [new_ip],
        "rrset_ttl": 300
    }

    try:
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        print(f"Updated A record for {subdomain}.{domain} to {new_ip}")
    except requests.RequestException as e:
        print(f"Error updating DNS record for {subdomain}.{domain}: {e}")
        print(f"Response content: {response.text}")

def main():
    display_ascii_art()

    # Get the current IP
    current_ip = get_current_ip()
    print(f"Current IP: {current_ip}")

    # Load credentials
    credentials = load_credentials(sys.argv[0])
    if not credentials:
        print("Error: Unable to load credentials")
        sys.exit(1)

    # Get domain and API key from credentials
    domain = credentials.get('DOMAIN')
    api_key = credentials.get('API_KEY')

    if not domain or not api_key:
        print("Error: Missing domain or API key in config file")
        sys.exit(1)

    # Test API key
    if not test_api_key(api_key):
        print("Please check your API key and ensure it has the necessary permissions.")
        sys.exit(1)

    # Get all DNS records
    all_records = get_all_records(domain, api_key)

    # Filter and update A records
    a_records = [record for record in all_records if record['rrset_type'] == 'A']
    
    if not a_records:
        print(f"No A records found for {domain}")
        sys.exit(0)

    print(f"Found {len(a_records)} A record(s) for {domain}")

    for record in a_records:
        subdomain = record['rrset_name']
        current_ip_in_record = record['rrset_values'][0]
        
        if current_ip_in_record != current_ip:
            print(f"Updating {subdomain}.{domain} from {current_ip_in_record} to {current_ip}")
            update_dns_record(domain, subdomain, current_ip, api_key)
        else:
            print(f"A record for {subdomain}.{domain} is already up to date ({current_ip})")

    print("DNS update process completed.")

if __name__ == "__main__":
    main()