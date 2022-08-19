# Extended_Substitution_Cipher

### Setup and Bring server up
chmod +x setup.sh
./setup.sh

### If setup is already complete and just server needs to brought up
#### Run the following inside virtual environment
python api.py

### Run client module to capture the flag in new shell
source env/bin/activate
python client.py
