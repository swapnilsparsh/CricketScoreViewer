# Setup script for Linux
## Untested
## TODO: Test script on Linux machine

if [[ "$PWD" =~ .*/setup ]]; then 
    cd ..
fi
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt