---
# ⌨️ Keyboard Logger GUI (Educational Python Project)

A Python-based GUI application that allows users to start and stop keyboard activity logging through a graphical interface.
This project is built strictly for educational and authorized cybersecurity learning, with a strong focus on readability, safety, and clean system design.

---

## ⚠️ Ethical & Legal Disclaimer

 This project is intended ONLY for

 Educational purposes
 Personal systems you own
 Systems where you have explicit permission

❌ Any form of unauthorized monitoring, spying, or misuse is illegal and unethical.
The author takes no responsibility for misuse.

---

## ✨ Features

 🖥️ Simple GUI using Tkinter

 ▶️ Start  Stop logging with buttons

 🟢 Live status indicator
 📁 Automatic per-session log files

 ⌨️ Human-readable key names (SPACE, ENTER, etc.)

 ⏱️ Millisecond-precision timestamps

 🧵 Thread-safe background logging

 📄 Clean session headers & footers

 ⚡ Buffered file writing for performance

---

## 🖼️ GUI Overview

```
+-----------------------------+
   Keyboard Logger GUI       
-----------------------------
 Status  RUNNING            
 Log File  key_events_...   
                             
 [ Start Logging ]           
 [ Stop Logging ]            
+-----------------------------+
```

---

## 📄 Sample Log Output

```txt
==================================
 Keyboard Session Log
 Started  2025-12-28 181005
==================================

[181007.122] PRESSED   H
[181007.289] RELEASED  H
[181007.410] PRESSED   I
[181007.580] RELEASED  I
[181008.031] PRESSED   SPACE
[181008.221] RELEASED  SPACE
[181008.612] PRESSED   ENTER
[181008.802] RELEASED  ENTER

==================================
 Session Ended  2025-12-28 181201
==================================
```

---

## 🛠️ Tech Stack

 Language Python 3.8+
 GUI Tkinter
 Keyboard Hooking `pynput`
 Concepts Used

   Multithreading
   Event listeners
   Thread synchronization (locks)
   File buffering & logging
   GUI state management
   Safe cleanup on exit

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DhruvParekh-star/keyboard-logger-gui.git
cd keyboard-logger-gui
```

### 2️⃣ Install Dependencies

```bash
pip install pynput
```

---

## ▶️ Usage

```bash
python keylogger_gui.py
```

### How it works

1. Click Start Logging
2. Perform keyboard actions
3. Click Stop Logging
4. Logs are saved automatically in the project directory

---

## 📁 Project Structure

```
keyboard-logger-gui
│
├── keylogger_gui.py
├── README.md
├── LICENSE
└── key_events_2025-12-28_18-10-05.txt
```

---

## 🎓 Educational Objectives

This project demonstrates

 GUI-controlled system input monitoring
 Safe keyboard event capture
 Thread-safe background processing
 Readable and structured logging
 Foundations of security monitoring tools

---

## 🚀 Future Enhancements

 🔐 Encrypted log files
 📊 Built-in log viewer GUI
 🧠 Keystroke-to-text reconstruction
 🖥️ Per-application logging
 🌐 Streamlit  web dashboard
 🚨 IDS-style behavioral analysis

---

## 📜 License

This project is licensed under the MIT License.
See the [`LICENSE`](LICENSE) file for details.

---

## 👨‍💻 Author
Dhruv Parekh

Computer Engineering Student

Cybersecurity & Systems Projects

---

## ⭐ Acknowledgment

Built for learning, experimentation, and ethical cybersecurity education.

---
