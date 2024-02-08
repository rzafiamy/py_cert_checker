#!/bin/bash

# Directory for the virtual environment
VENV_DIR="venv"

# Python script to run
PYTHON_SCRIPT="ssl_check.py"

# DOMAIN FILE
DOMAIN_FILE="domain.local"

# Output file
REPORT_FILE="report.dat"

# Check if the virtual environment exists, if not, create it
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

echo "Installing requirements from requirements.txt..."
pip install -r requirements.txt

echo "Running script and redirecting output to $REPORT_FILE..."
python $PYTHON_SCRIPT $DOMAIN_FILE > $REPORT_FILE

echo "Deactivating virtual environment..."
deactivate

echo "Done. Output is in $REPORT_FILE"
