sudo apt install python3-pip python3-venv

cd ~
mkdir 18.tt
cd 18.tt

python3 -m venv env
env/bin/python -m pip install aiohttp

sudo cp systemd.service  /lib/systemd/system/18.tt.service
sudo systemctl enable 18.tt
sudo systemctl start 18.tt


