# Worker.cash 2captcha solver

![Demo GIF](https://github.com/s3ij1nn/workercash-2captcha/raw/main/Demo.gif)

Using DroidVNC-NG. (You can install from f-droid.)

Local desktop ( Same network like 192.168.1.1/24)

This script not provide touch play button tool.

Use official Macrodroid script.

## create venv
```
python -m venv venv

venv/bin/activate
# Windows Powershell
venv\Scripts\Activate.ps1

pip install opencv-python numpy vncdotool 2captcha-python
```

## Setting

edit run.py
```
vnc_host = '192.168.10.118'

# 2captcha api key
api_key = 'YOUR_2CAPTCHA_KEY'
```

## Run
python run.py

## More info 
Do not delete "instruction.png"  
This file using detect captcha.

screen2.png and screen3.png is example.
