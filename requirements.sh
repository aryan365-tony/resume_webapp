#!/usr/bin/env bash

# Install Python dependencies
pip install -r requirements.txt
playwright install --with-deps
