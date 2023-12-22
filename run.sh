#!/bin/bash

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip to ensure the latest version is used
pip install --upgrade pip

# Install dependencies
pip install colored pyperclip

# Run your Python script
python main.py  