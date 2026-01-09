import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

LOG_FILE = "firewall.log"

def log_action(action):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {action}\n")

def allow_port():
    port = entry.get().strip()
    if port.isdigit():
        os.system(f"sudo ufw allow {port}")
        log_action(f"Allowed Port {port}")
        messagebox.showinfo("Success", f"Port {port} allowed")
    else:
        messagebox.showerror("Error", "Enter valid port number")

def block_port():
    port = entry.get().strip()
    if port.isdigit():
        os.system(f"sudo ufw deny {port}")
        log_action(f"Blocked Port {port}")
        messagebox.showwarning("Blocked", f"Port {port} blocked")
    else:
        messagebox.showerror("Error", "Enter valid port number")

def allow_ip():
    ip = entry.get().strip()
    if ip:
        os.system(f"sudo ufw allow from {ip}")
        log_action(f"Allowed IP {ip}")
        messagebox.showinfo("Success", f"IP {ip} allowed")
    else:
        messagebox.showerror("Error", "Enter valid IP")

def block_ip():
    ip = entry.get().strip()
    if ip:
        os.system(f"sudo ufw deny from {ip}")
        log_action(f"Blocked IP {ip}")
        messagebox.showerror("Blocked", f"IP {ip} blocked")
    else:
        messagebox.showerror("Error", "Enter valid IP")

def show_rules():
    os.system("sudo ufw status numbered")

root = tk.Tk()
root.title("🔥 Firewall Rule Manager")
root.geometry("380x320")
root.resizable(False, False)

tk.Label(root, text="Enter Port or IP", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=35)
entry.pack(pady=5)

tk.Button(root, text="Allow Port", width=20, command=allow_port).pack(pady=4)
tk.Button(root, text="Block Port", width=20, command=block_port).pack(pady=4)
tk.Button(root, text="Allow IP", width=20, command=allow_ip).pack(pady=4)
tk.Button(root, text="Block IP", width=20, command=block_ip).pack(pady=4)
tk.Button(root, text="Show Rules", width=20, command=show_rules).pack(pady=10)

root.mainloop()
