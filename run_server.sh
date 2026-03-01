#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
PYTHON_BIN=""
REQ_FILE="$SCRIPT_DIR/requirements.txt"
REQ_HASH_FILE="$VENV_DIR/.requirements.sha256"

log() {
  echo "[illustrator-mcp] $1"
}

to_windows_path() {
  local input_path="$1"

  if command -v cygpath >/dev/null 2>&1; then
    cygpath -w "$input_path"
    return 0
  fi

  if command -v wslpath >/dev/null 2>&1; then
    wslpath -w "$input_path"
    return 0
  fi

  # Fallback for shells that already expose Windows-style paths.
  echo "$input_path"
}

find_python() {
  if [ -x "$VENV_DIR/Scripts/python.exe" ]; then
    PYTHON_BIN="$VENV_DIR/Scripts/python.exe"
    return 0
  fi

  if command -v python >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python)"
    return 0
  fi

  if command -v py >/dev/null 2>&1; then
    PYTHON_BIN="py -3"
    return 0
  fi

  return 1
}

ensure_venv() {
  if [ ! -x "$VENV_DIR/Scripts/python.exe" ]; then
    log "Creating virtual environment in .venv"
    if command -v python >/dev/null 2>&1; then
      python -m venv "$VENV_DIR"
    elif command -v py >/dev/null 2>&1; then
      py -3 -m venv "$VENV_DIR"
    else
      log "Python was not found. Install Python 3.11+ and retry."
      exit 1
    fi
  fi

  PYTHON_BIN="$VENV_DIR/Scripts/python.exe"
}

requirements_hash() {
  # Git Bash on Windows ships with sha256sum.
  sha256sum "$REQ_FILE" | awk '{print $1}'
}

has_pip() {
  $PYTHON_BIN -m pip --version >/dev/null 2>&1
}

ensure_pip() {
  if has_pip; then
    return 0
  fi

  log "pip not found in .venv. Bootstrapping with ensurepip..."
  if ! $PYTHON_BIN -m ensurepip --upgrade >/dev/null 2>&1; then
    log "Failed to bootstrap pip. Please install pip for this Python and retry."
    exit 1
  fi

  if ! has_pip; then
    log "pip is still unavailable after ensurepip."
    exit 1
  fi
}

requirements_ok() {
  local expected_hash current_hash

  if [ ! -f "$REQ_HASH_FILE" ]; then
    return 1
  fi

  expected_hash="$(cat "$REQ_HASH_FILE" 2>/dev/null || true)"
  current_hash="$(requirements_hash)"

  if [ "$expected_hash" != "$current_hash" ]; then
    return 1
  fi

  if ! has_pip; then
    return 1
  fi

  if ! $PYTHON_BIN -m pip check >/dev/null 2>&1; then
    return 1
  fi

  # Validate key runtime imports for this server.
  if ! $PYTHON_BIN -c "import mcp, PIL, win32com.client" >/dev/null 2>&1; then
    return 1
  fi

  return 0
}

install_requirements() {
  local req_file_win
  req_file_win="$(to_windows_path "$REQ_FILE")"

  ensure_pip
  log "Installing dependencies from requirements.txt"
  $PYTHON_BIN -m pip install --upgrade pip
  $PYTHON_BIN -m pip install -r "$req_file_win"
  requirements_hash > "$REQ_HASH_FILE"
}

main() {
  local server_file_win

  ensure_venv
  ensure_pip

  if requirements_ok; then
    log "Dependencies are already satisfied. Skipping install."
  else
    install_requirements
  fi

  server_file_win="$(to_windows_path "$SCRIPT_DIR/illustrator/server.py")"

  log "Starting Illustrator MCP server..."
  log "To stop the server, press Ctrl+C in this terminal."
  exec $PYTHON_BIN "$server_file_win"
}

main "$@"
