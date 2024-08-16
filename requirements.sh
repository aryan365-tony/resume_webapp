#!/bin/bash
# Install Python dependencies
pip install -r requirements.txt

python -m playwright install chromium --with-deps

