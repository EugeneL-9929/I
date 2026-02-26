#!/bin/bash
python3 --version

# checking the virtual environment
if [ ! -d "I_venv" ]; then
    echo "we are building a new virtual python env."
    python3 -m venv I_venv
    source I_venv/bin/activate
else
    echo "I_env virtual python env found."
    source I_venv/bin/activate
fi

# checking library in the venv
echo "checking the necessary libraries."
LBS_NAME="os json pathlib curl_cffi"
for LB in $LBS_NAME; do
    if python3 -c "import $LB" >/dev/null 2>&1; then
        echo "$LB library exists."
    else
        pip install $LB --upgrade
    fi
done

# execution
cd py
./venv_py.sh
cd ..

deactivate

cd py
./py.sh
cd ..
python3 -m main