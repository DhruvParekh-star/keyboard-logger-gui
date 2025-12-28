import threading
import time
from datetime import datetime
from pynput import keyboard
import tkinter as tk
from tkinter import messagebox

# ===============================
# Global State
# ===============================
listener = None
logging_active = False
key_events = []
held_keys = set()
lock = threading.Lock()
LOG_FILE = None
FLUSH_THRESHOLD = 20

# ===============================
# Helper Functions
# ===============================
def readable_time():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]

def clean_key(key):
    k = str(key)
    if k.startswith("Key."):
        return k.replace("Key.", "").upper()
    return k

def write_to_file(events):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        for e in events:
            f.write(f"[{e['time']}] {e['type'].upper():<8} : {e['key']}\n")

def maybe_flush():
    global key_events
    with lock:
        if len(key_events) >= FLUSH_THRESHOLD:
            write_to_file(key_events)
            key_events.clear()

# ===============================
# Keyboard Callbacks
# ===============================
def on_press(key):
    if not logging_active:
        return

    k = clean_key(key)
    with lock:
        if k not in held_keys:
            key_events.append({
                "type": "pressed",
                "key": k,
                "time": readable_time()
            })
            held_keys.add(k)
    maybe_flush()

def on_release(key):
    if not logging_active:
        return

    k = clean_key(key)
    with lock:
        key_events.append({
            "type": "released",
            "key": k,
            "time": readable_time()
        })
        held_keys.discard(k)
    maybe_flush()

# ===============================
# Logger Control
# ===============================
def start_logging():
    global listener, logging_active, LOG_FILE

    if logging_active:
        messagebox.showinfo("Info", "Keylogger is already running.")
        return

    SESSION_TIME = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    LOG_FILE = f"key_events_{SESSION_TIME}.txt"

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("=" * 34 + "\n")
        f.write(" Keyboard Session Log\n")
        f.write(f" Started : {datetime.now()}\n")
        f.write("=" * 34 + "\n\n")

    logging_active = True
    status_label.config(text="Status : RUNNING", fg="green")
    file_label.config(text=f"Log File : {LOG_FILE}")

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

def stop_logging():
    global listener, logging_active, key_events

    if not logging_active:
        messagebox.showinfo("Info", "Keylogger is not running.")
        return

    logging_active = False

    if listener:
        listener.stop()
        listener = None

    with lock:
        if key_events:
            write_to_file(key_events)
            key_events.clear()

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + "=" * 34 + "\n")
        f.write(f" Session Ended : {datetime.now()}\n")
        f.write("=" * 34 + "\n")

    status_label.config(text="Status : STOPPED", fg="red")
    messagebox.showinfo("Stopped", "Keylogger stopped and log saved.")

# ===============================
# GUI Setup
# ===============================
root = tk.Tk()
root.title("Keyboard Logger (Educational)")
root.geometry("360x220")
root.resizable(False, False)

title = tk.Label(root, text="Keyboard Logger GUI", font=("Arial", 14, "bold"))
title.pack(pady=10)

status_label = tk.Label(root, text="Status : STOPPED", fg="red", font=("Arial", 11))
status_label.pack(pady=5)

file_label = tk.Label(root, text="Log File : None", font=("Arial", 9))
file_label.pack(pady=5)

start_btn = tk.Button(root, text="Start Logging", width=20, command=start_logging)
start_btn.pack(pady=8)

stop_btn = tk.Button(root, text="Stop Logging", width=20, command=stop_logging)
stop_btn.pack(pady=5)

def on_close():
    if logging_active:
        stop_logging()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
