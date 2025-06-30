#!/usr/bin/env bash
set -e

echo "Activating venv and installing dependencies"
python3 -m venv venv
. venv/bin/activate

echo "Installing requirements and Playwright browsers"
pip install -r requirements.txt

# ✅ Important: include system dependencies
playwright install --with-deps

echo "Running $SUITE suite"
pytest -m "$SUITE" playwright/