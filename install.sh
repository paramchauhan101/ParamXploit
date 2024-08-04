#!/bin/bash

# Install required system packages
echo "Installing system packages..."
sudo apt update
sudo apt install -y nikto nmap python3-pip

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install colorama

# Make the script executable
echo "Making the script executable..."
chmod +x paramxploit.py

echo "Installation completed successfully!"
