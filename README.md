# 🚀 Internet Optimizer (v1.2.1)

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.2.1-orange)

A high-performance utility designed to optimize Windows network settings, reducing latency (ping) and improving connection stability for online gaming and real-time applications.

---

## 🛡️ Transparency and Security

> [!IMPORTANT]
> This software performs low-level modifications to the Windows Registry and utilizes network commands (netsh). For these reasons, Windows Defender or third-party antivirus software may flag the file as "suspicious."

This behavior is a common false positive in system optimization tools. The code is 100% open-source. If you have any doubts, I highly recommend cloning the repository and running the script directly from the source code (Python), allowing you to audit exactly what is being changed on your system.

---

## ⚙️ Features (v1.2.2)

* 🗃️ Portable Safety Backup: Automatically creates a .reg backup file before any modifications are applied.
* ⚡ Network Throttling Control: Disables Windows' network packet throttling for maximum system responsiveness.
* 🎯 Nagle's Algorithm Optimization: Configures TCP parameters for immediate packet delivery.
* 🌐 TCP Stack Stabilization: Optimizes Receive Side Scaling (RSS) and disables Fast Open and ECN to prevent session drops and IP mismatch errors.
* 📏 Dynamic MTU Discovery: Active diagnostic scan to determine the ideal MTU, eliminating packet fragmentation.
* 🔄 Deep Cleanup: Automatically executes flushdns, winsock reset, and ip reset with real-time visual feedback.
* 🌐 DNS Optimization: Optional configuration of high-performance DNS servers (Google/Cloudflare).

---

## 🛠️ How to Use

### 🎮 Option A: End User (Executable)
Ideal for those who want quick optimization without installing dependencies.

1. Download the internet_optimizer.exe from the Releases tab.
2. Right-click the file and select "Run as administrator".
3. Follow the instructions in the terminal. The script will handle the complete automation.
4. Restart your PC to apply the network changes.

### 💻 Option B: Developer (Source Code)
Ideal for those who want to audit or customize the code.

1. Ensure you have Python 3.8+ installed.
2. Clone the repository and run:
   python internet_optimizer.py
   (The script will automatically request administrator privileges).

---

## 🏗️ Developer's Guide (Compiling)

If you have modified the source code and need to generate a new executable:

1. Install PyInstaller:
   pip install pyinstaller

2. Generate the binary (bundled into a single file):
   pyinstaller --onefile --icon=moose.ico internet_optimizer.py

The generated file will be available in the dist/ folder.

---

## 📜 License
This project is distributed under the MIT License. You are free to use, modify, and distribute the code, provided that the original credits are maintained.
