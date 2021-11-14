#! /bin/bash

PROGRAM=$(dirname "$0")
cd "${PROGRAM}" || exit
source ./venv/bin/activate
python3 main.py
deactivate