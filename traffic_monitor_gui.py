import socket
import struct
import tkinter as tk
from datetime import datetime

def start_monitor():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, _ = conn.recvfrom(65536)
        if raw_data[12:14] == b'\x08\x00':  # IPv4
            src_ip = ".".join(map(str, raw_data[26:30]))
            dst_ip = ".".join(map(str, raw_data[30:34]))
            text.insert(tk.END, f"{datetime.now()} | {src_ip} → {dst_ip}\n")
            text.see(tk.END)

root = tk.Tk()
root.title("📡 Real-Time Traffic Monitor")
root.geometry("600x400")

text = tk.Text(root)
text.pack(expand=True, fill=tk.BOTH)

tk.Button(root, text="Start Monitoring", command=start_monitor).pack(pady=5)

root.mainloop()
