from wol import WakeOnLan
MAC = "00-00-00-00-00-00" # Input the target PC's MAC address
ADDRS = "192.168.0.255"
PORT = 7

'''
- 공유기 사용자는 ADDRS 인자에 브로드캐스트 주소를 사용해야한다.
Ex) Iptime 공유기의 경우에는 브로드캐스 주소가 192.168.0.255 이다.
이를 포트 7번에 전송하게 된다면, 현재 공유기에 연결된 모든 디바이스가 매직패킷을 수신하게된다.
매직 패킷 원리는 16진수 FF 상수값이 6번 반복 + 대상 컴퓨터의 맥어드레스가 16번 반복(16진수) 이니,
타깃 PC만 전원이 켜지게 된다.

- 공유기 미사용자는 일반 Target IP를 사용하면 된다.
'''

if __name__ == "__main__":
    WakeOnLan(MAC).turn_on(ADDRS, PORT)