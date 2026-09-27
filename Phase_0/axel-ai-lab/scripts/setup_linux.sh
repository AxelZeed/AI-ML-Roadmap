#!/usr/bin/env bash

set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

echo "Checking Python..."

"$PYTHON_BIN" -c "
import sys

required = (3, 13)

if sys.version_info < required:
    raise SystemExit(
        f'Python 3.13+ required. '
        f'Found {sys.version.split()[0]}'
    )

print(f'Python {sys.version.split()[0]} detected.')
"

echo
echo "Creating virtual environment..."

"$PYTHON_BIN" -m venv .venv

echo
echo "Installing Axel AI Lab..."

.venv/bin/python -m pip install --upgrade pip

.venv/bin/python -m pip install \
    -e ".[dev,tools]"

if [ ! -f .env ]; then
    echo
    echo "Creating .env from .env.example..."
    cp .env.example .env
fi

echo
echo "Setup complete."
echo
echo "Activate with:"
echo "source .venv/bin/activate"
echo
echo "Then run:"
echo "axel-ai-lab --verbose"