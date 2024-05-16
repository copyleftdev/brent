#!/bin/bash

# This script starts the Brent server.

# Set the project root directory
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Activate virtual environment if it exists
if [ -d "$PROJECT_ROOT/venv" ]; then
  source "$PROJECT_ROOT/venv/bin/activate"
fi

# Run the main.py script to start the server
echo "Starting Brent server..."
python "$PROJECT_ROOT/brent/main.py" "$@"

# Deactivate virtual environment if it was activated
if [ -d "$PROJECT_ROOT/venv" ]; then
  deactivate
fi
