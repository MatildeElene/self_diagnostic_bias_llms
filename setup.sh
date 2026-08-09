#!/bin/bash
set -e #stopping if failure
mkdir -p out

python -m pip install --upgrade pip
pip install -r requirements.txt

echo "setup is complete."