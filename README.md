# Worker.cash DroidVNC-NG 2captcha solver

Install Termux or Local desktop ( Same network like 192.168.1.1/24)

## create venv
```
python -m venv venv

venv/bin/activate
# Windows Powershell
venv/Scripts/Activate.ps1

pip install -r requirements.txt
```

## Setting

edit run.py
```
vnc_host = '192.168.10.118'
# on termux
vnc_host = '127.0.0.1'

# 2captcha api key
api_key = 'YOUR_2CAPTCHA_KEY'
```

## Run
python run.py

## More info 
Do not delete "instruction.png"  
This file use captcha is displayed check.

screen2.png and screen3.png is example.