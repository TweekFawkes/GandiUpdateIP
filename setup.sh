#!/bin/bash

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create config file (replace with actual values)
echo "DOMAIN=your_domain.com" > GandiUpdateIP.config
echo "API_KEY=your_gandi_api_key_here" >> GandiUpdateIP.config

# Run the script
python GandiUpdateIP.py