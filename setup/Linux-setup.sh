#!/bin/bash
# Setup script for Linux

if [[ "$PWD" =~ .*/setup ]]; then 
    cd ..
fi
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt