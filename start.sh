#!/bin/bash

# Define variables
ENV=DEVELOPMENT
PYTHONDONTWRITEBYTECODE=1
PYTHON_EXECUTABLE=""
DASHBOARD_FILE="app/src/main.py"
REQUIREMENTS_FILE="app/requirements.txt"

# Define functions
set_python_executable() {
  if [ "$(uname -s)" = "Linux" ]; then
    PYTHON_EXECUTABLE=venv/bin/python
  elif [ "$(uname -s)" = "Windows" ]; then
    PYTHON_EXECUTABLE=venv/Scripts/python
  elif [ "$(uname -s)" = "Darwin" ]; then
    PYTHON_EXECUTABLE=venv/bin/python
  else
    echo "Unsupported operating system"
    exit 1
  fi
}

create_virtual_environment() {
  if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Installing requirements..."
    $PYTHON_EXECUTABLE -m pip install -r $REQUIREMENTS_FILE
  fi
}

start_dashboard() {
  echo "Starting Streamlit Dashboard..."
  echo "Environment: $ENV"
  PYTHONDONTWRITEBYTECODE=1 ENV=$ENV $PYTHON_EXECUTABLE -m streamlit run $DASHBOARD_FILE
}

# Main script
set_python_executable
create_virtual_environment
start_dashboard