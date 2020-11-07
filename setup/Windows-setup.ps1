# Setup script for Windows

if ($pwd -like "*\setup") { cd.. } # Goto root dir
python3.exe -m virtualenv venv
.\venv\Scripts\Activate.ps1
pip3 install -r requirements.txt