#!/bin/bash
# Install Python dependencies
pip install -r requirements.txt

yarn install
yarn playwright install --with-deps

