import struct
import socket
import os

class WakeOnLan():
    """
    WOL (Wake On Lan) Class
    """

    def __init__(self, mac_addrs):
        """
        Class Init

        Magic Packet은 16진수 FF 상수 값이 6번 반복 + 타깃 컴퓨터의 MAC Address(16진수)가 16번 반복이다.

        Args:
            mac_addrs (String): Target MAC Address
        """
        self.mac_addrs = mac_addrs
        
        mac = mac_addrs.split("-")
        hw_addr = struct.pack("BBBBBB", int(mac[0], 16), 
        int(mac[1], 16), int(mac[2], 16), 
        int(mac[3], 16), int(mac[4], 16), 
        int(mac[5], 16))
        self.magic_packet = b"\xFF" * 6 + hw_addr * 16
        
        
    def operate(self, addrs, port):
        """
        WOL 설정이 된 PC의 전원을 켜주는 함수.

        Args:
            addrs (String): Target IP Address
            port ([type]): Port
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        s.sendto(self.magic_packet, (addrs, port))
        s.close()
