#!/bin/bash

# Change to the directory containing the script
cd "$(dirname "$0")"

# Activate the virtual environment
. ./venv/bin/activate

# Run the Python script
python main.py
