@echo off
color E
git clone https://github.com/camenduru/stable-diffusion-webui-catppuccin extensions/stable-diffusion-webui-catppuccin
start /b webui-user.bat
python lightspeed-droidui\waitrun.py