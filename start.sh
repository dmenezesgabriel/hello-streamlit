#!/bin/bash

# Define variables
ENV=DEVELOPMENT
PYTHONDONTWRITEBYTECODE=1
PYTHON_EXECUTABLE="/usr/bin/python3"
PYTHON_VENV_EXECUTABLE=""
DASHBOARD_FILE="app/src/Dashboard.py"
REQUIREMENTS_FILE="app/requirements.txt"

# Define functions
set_PYTHON_VENV_EXECUTABLE() {
  if [ "$(uname -s)" = "Linux" ]; then
    PYTHON_VENV_EXECUTABLE=venv/bin/python
  elif [ "$(uname -s)" = "Windows" ]; then
    PYTHON_VENV_EXECUTABLE=venv/Scripts/python
  elif [ "$(uname -s)" = "Darwin" ]; then
    PYTHON_VENV_EXECUTABLE=venv/bin/python
  else
    echo "Unsupported operating system"
    exit 1
  fi
}

create_virtual_environment() {
  if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON_EXECUTABLE -m venv venv
    echo "Installing requirements..."
    $PYTHON_VENV_EXECUTABLE -m pip install -r $REQUIREMENTS_FILE
  fi
}

start_dashboard() {
  echo "Starting Streamlit Dashboard..."
  echo "Environment: $ENV"
  PYTHONDONTWRITEBYTECODE=1 \
  ENV=$ENV \
  $PYTHON_VENV_EXECUTABLE -m streamlit run $DASHBOARD_FILE \
  --logger.level=debug
}

# Main script
set_PYTHON_VENV_EXECUTABLE
create_virtual_environment
start_dashboard