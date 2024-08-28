# GandiUpdateIP

This script updates the DNS A record for a specified domain using the Gandi API based on the user's current IP address.

## Setup

1. Clone the repository or download the script:

   ```
   git clone https://github.com/TweekFawkes/GandiUpdateIP.git
   cd GandiUpdateIP
   ```

2. Create a virtual environment and activate it:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:

   ```
   pip install -r requirements.txt
   ```

4. Create a `GandiUpdateIP.config` file with your Gandi API credentials:

   ```
   DOMAIN=your_domain.com
   API_KEY=your_gandi_api_key
   ```

5. Run the script:
   ```
   python GandiUpdateIP.py
   ```

## Features

- Retrieves current IP address from ipcurl.net
- Updates DNS A record using Gandi API
- Displays ASCII art on script execution
- Secure credential handling

## Running Periodically with Cron

To run the script periodically, you can set up a cron job. Here's how:

1. Make sure the script is executable:

   ```
   chmod +x /path/to/GandiUpdateIP.py
   ```

2. Open your crontab file:

   ```
   crontab -e
   ```

3. Add a line to run the script periodically. For example, to run it every hour:

   ```
   0 * * * * /path/to/venv/bin/python /path/to/GandiUpdateIP.py >> /path/to/GandiUpdateIP.log 2>&1
   ```

   This will run the script every hour and log the output to a file.

   To run it every 15 minutes:

   ```
   */15 * * * * /path/to/venv/bin/python /path/to/GandiUpdateIP.py >> /path/to/GandiUpdateIP.log 2>&1
   ```

   Adjust the timing and paths according to your needs.

4. Save and exit the crontab editor.

Make sure to replace `/path/to/` with the actual path to your script and virtual environment.

## Requirements

See `requirements.txt` for a list of required Python packages.

## Note

This script ignores SSL certificate validation when fetching the IP address. Use with caution in production environments.

## Troubleshooting

If you encounter issues with the cron job:

1. Ensure all paths in the cron command are absolute.
2. Check the log file for any error messages.
3. Make sure the user running the cron job has the necessary permissions.
4. Verify that the virtual environment is activated in the cron command.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).


## Dev Container Setup

Run these commands...
```
sudo apt update
sudo apt install -y python3-pip
python3 -m pip install -r requirements.txt
python3 GandiUpdateIP.py
```

Output should look like the following...
```
vscode ➜ /workspaces/GandiUpdateIP (main) $ python3 GandiUpdateIP.py
   ______                ___ __  __          __      __       ________ 
  / ____/___ _____  ____/ (_) / / /___  ____/ /___ _/ /____  /  _/ __ \
 / / __/ __ `/ __ \/ __  / / / / / __ \/ __  / __ `/ __/ _ \ / // /_/ /
/ /_/ / /_/ / / / / /_/ / / /_/ / /_/ / /_/ / /_/ / /_/  __// // ____/ 
\____/\__,_/_/ /_/\__,_/_/\____/ .___/\__,_/\__,_/\__/\___/___/_/      
                              /_/                                      

/home/vscode/.local/lib/python3.10/site-packages/urllib3/connectionpool.py:1099: InsecureRequestWarning: Unverified HTTPS request is being made to host 'ipcurl.net'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
Current IP: 65.130.48.113
Found 12 A record(s) for example.org
Updating @.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for @.example.org to 65.130.48.113
Updating elite.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for elite.example.org to 65.130.48.113
Updating franklin.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for franklin.example.org to 65.130.48.113
Updating keyidtoaccountid.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for keyidtoaccountid.example.org to 65.130.48.113
Updating labs.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for labs.example.org to 65.130.48.113
Updating marcie.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for marcie.example.org to 65.130.48.113
Updating nmaptohashtags.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for nmaptohashtags.example.org to 65.130.48.113
Updating peppermint.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for peppermint.example.org to 65.130.48.113
Updating rawkhawk.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for rawkhawk.example.org to 65.130.48.113
Updating schroeder.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for schroeder.example.org to 65.130.48.113
Updating whoami.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for whoami.example.org to 65.130.48.113
Updating www.example.org from 65.130.244.125 to 65.130.48.113
Updated A record for www.example.org to 65.130.48.113
DNS update process completed.
vscode ➜ /workspaces/GandiUpdateIP (main) $ 
```
