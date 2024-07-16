#!/usr/bin/env bash

# Install Python dependencies
pip install -r requirements.txt

# Download the static binary of wkhtmltopdf for Ubuntu Jammy (22.04)
wget wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb

# Extract the executable using ar and tar
ar x wkhtmltox_0.12.6-1.bionic_amd64.deb
tar -xf data.tar.xz

# Create a bin directory if it doesn't exist and move the wkhtmltopdf binary to it
mkdir -p bin
mv usr/local/bin/wkhtmltopdf bin/

# Ensure wkhtmltopdf has execute permissions
chmod +x bin/wkhtmltopdf
