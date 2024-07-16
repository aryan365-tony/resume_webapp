#!/usr/bin/env bash

# Install Python dependencies
pip install -r requirements.txt

# Download wkhtmltopdf
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb

# Extract the executable
dpkg -x wkhtmltox_0.12.6-1.bionic_amd64.deb wkhtmltox

# Move the wkhtmltopdf binary to the bin directory
mkdir -p bin
mv wkhtmltox/usr/local/bin/wkhtmltopdf bin/

# Ensure wkhtmltopdf has execute permissions
chmod +x bin/wkhtmltopdf
