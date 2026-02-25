#!/bin/bash
python3 --version
# python3 -m venv I_venv

if [ ! -d "I_venv" ]; then
    echo "no I_venv virtual environment found!"
    python3 -m venv I_venv
else
    echo "I_venv virtual machine found!"
    source I_venv/bin/activate
fi



# pip install curl_cffi --upgrade

python3 -m ratio.py

deactivate

make clean
make
./compile/my_program