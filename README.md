# MagicPacket Transmitter - WOL 매직 패킷 송신기
<br><br>

<div align=center>
    <strong># Python</strong> &nbsp;
    <strong># IOT</strong> &nbsp;
    <strong># WOL</strong> &nbsp;
</div>
<br>

## What is this?
WOL(Wake On Lan)을 지원하는 PC에 Magic Packet을 전송해주는 프로그램입니다.

<br>

## Dependency
```shell
python 3.8.X
```
<br>

## How to use
```python
# Sample Usage
from wol import WakeOnLan

MAC = "00-00-00-00-00-00"
ADDRS = "192.168.0.255"
PORT = 7

WakeOnLan(MAC).operate(ADDRS, PORT)
```

```python
# Sample Sever Code
from fastapi import FastAPI
from wol import WakeOnLan

app = FastAPI()

@app.get("/turn_on/")
async def turn_on(mac: str, addrs: str, port: int = 80):
    if not (mac and addrs and port):
        return False
    
    try:
        WakeOnLan(mac).operate(addrs, port)
        return True
    except:
        return False
```
<br>

## About Me
🙋🏻‍♂️ Name: 837477

📧 E-mail: 8374770@gmail.com

🐱 Github: https://github.com/837477

<br>

## Contributing
1. Fork this repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -m 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
