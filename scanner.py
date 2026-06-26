# Network Scanner using Nmap
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import nmap

root=tk.Tk()
root.title("Network Scanner using Nmap")
root.geometry("850x600")

tk.Label(root,text="Network Scanner using Nmap",font=("Arial",20,"bold")).pack(pady=10)
frame=tk.Frame(root); frame.pack(pady=10)
tk.Label(frame,text="Target IP / Domain:").grid(row=0,column=0,padx=5)
target_entry=tk.Entry(frame,width=40); target_entry.grid(row=0,column=1,padx=5)
scan_button=tk.Button(frame,text="Start Scan"); scan_button.grid(row=0,column=2,padx=5)
output_box=scrolledtext.ScrolledText(root,width=100,height=28)
output_box.pack(pady=10)

def scan_network():
    target=target_entry.get().strip()
    if not target:
        messagebox.showerror("Error","Please enter Target IP or Domain")
        return
    output_box.delete("1.0",tk.END)
    output_box.insert(tk.END,f"Scanning {target}\n\n")
    try:
        scanner=nmap.PortScanner()
        scanner.scan(hosts=target,arguments="-O -sV")
        for host in scanner.all_hosts():
            output_box.insert(tk.END,f"Host : {host}\n")
            output_box.insert(tk.END,f"State : {scanner[host].state()}\n\n")
            if "osmatch" in scanner[host] and scanner[host]["osmatch"]:
                output_box.insert(tk.END,"OS Detection\n")
                output_box.insert(tk.END,scanner[host]["osmatch"][0]["name"]+"\n\n")
            for proto in scanner[host].all_protocols():
                output_box.insert(tk.END,f"Protocol : {proto}\n")
                for port in sorted(scanner[host][proto].keys()):
                    d=scanner[host][proto][port]
                    output_box.insert(tk.END,f"Port : {port}\nState : {d.get('state')}\nService : {d.get('name')}\n")
                    if d.get("version"):
                        output_box.insert(tk.END,f"Version : {d['version']}\n")
                    output_box.insert(tk.END,"-"*40+"\n")
    except Exception as e:
        messagebox.showerror("Error",str(e))

scan_button.config(command=lambda: threading.Thread(target=scan_network,daemon=True).start())
root.mainloop()

# -----------------------------
# Run scan in separate thread
# -----------------------------
def start_scan():
    thread = threading.Thread(
        target=scan_network
    )
    thread.daemon = True
    thread.start()

# Button Command
scan_button.config(command=start_scan)

# Run GUI
root.mainloop()
