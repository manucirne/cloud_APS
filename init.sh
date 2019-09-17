sudo apt-get update -y
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
pip3 install flask -y
pip3 install flask_restful -y
export IPADDR="http://127.0.0.1:5000"
python3 webserver.py
