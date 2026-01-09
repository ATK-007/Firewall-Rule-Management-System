import socket
import struct
import os
from collections import defaultdict
from datetime import datetime

THRESHOLD = 20  # packets per IP
ip_counter = defaultdict(int)

def block_ip(ip):
    os.system(f"sudo ufw deny from {ip}")
    with open("firewall.log", "a") as f:
        f.write(f"{datetime.now()} - Auto-blocked IP {ip}\n")

def get_source_ip(packet):
    ip_header = packet[14:34]
    src_ip = struct.unpack("!12x4s", ip_header)[0]
    return socket.inet_ntoa(src_ip)

conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
print("🚨 Traffic Analyzer Started (DDoS Detection ON)")

while True:
    raw_data, _ = conn.recvfrom(65536)
    if raw_data[12:14] == b'\x08\x00':  # IPv4
        src_ip = get_source_ip(raw_data)
        ip_counter[src_ip] += 1

        with open("traffic.log", "a") as log:
            log.write(f"{datetime.now()} - Packet from {src_ip}\n")

        if ip_counter[src_ip] == THRESHOLD:
            print(f"⚠️ DDoS Suspected from {src_ip}")
            block_ip(src_ip)
