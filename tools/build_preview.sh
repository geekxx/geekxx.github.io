#!/usr/bin/env bash
# Build preview wrapper
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

# create venv if it doesn't exist
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# activate
. .venv/bin/activate

# ensure pip and deps
pip install --upgrade pip
pip install -r requirements.txt

# run the builder
python tools/build_preview.py

echo "Built previews into _site_preview/"
