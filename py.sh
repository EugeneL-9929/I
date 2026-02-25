#!/bin/bash
python3 --version

if [ ! -d "I_venv" ]; then
    python3 -m venv I_venv
    source I_venv/bin/activate
    pip install curl_cffi --upgrade
else
    source I_venv/bin/activate
fi

python3 -m main.py

deactivate