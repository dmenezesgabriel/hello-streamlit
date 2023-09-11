#!/bin/bash

# Define variables
ENV=DEVELOPMENT
PYTHONDONTWRITEBYTECODE=1
PYTHON_EXECUTABLE="python"
PYTHON_VENV_EXECUTABLE=""
DASHBOARD_FILE="src/Main.py"
REQUIREMENTS_FILE="requirements.txt"

# Define functions
set_PYTHON_VENV_EXECUTABLE() {
  if [ "$(uname -s)" = "Linux" ]; then
    PYTHON_VENV_EXECUTABLE=venv/bin/python
  elif [ "$(uname -s)" = "Windows" ]; then
    PYTHON_VENV_EXECUTABLE=venv/Scripts/python
  elif [ "$(uname -s)" = "Darwin" ]; then
    PYTHON_VENV_EXECUTABLE=venv/bin/python
  elif [[ "$(uname -s)" = "MINGW64"* ]]; then
    PYTHON_VENV_EXECUTABLE=venv/Scripts/python
  else
    echo "Unsupported operating system"
    exit 1
  fi
}

create_virtual_environment() {
  if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON_EXECUTABLE -m venv venv
  fi
}

install_dependencies() {
  echo "Installing dependencies..."
  $PYTHON_VENV_EXECUTABLE -m pip install -q -r $REQUIREMENTS_FILE
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
install_dependencies
start_dashboard
