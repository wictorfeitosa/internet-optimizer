# 🚀 Internet Optimizer

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=blue)
![License](https://img.shields.io/badge/License-MIT-green)

A high-performance utility designed to optimize Windows network settings, reducing **latency (ping)** and improving connection stability for gaming and real-time applications.

---

## 🛡️ Transparency and Security

> [!IMPORTANT]
> This software performs low-level modifications to the **Windows Registry** and utilizes network commands (`netsh`). For these reasons, **Windows Defender** or third-party antivirus software may flag the executable file as "suspicious."

**This behavior is a common false positive in optimization tools.** The code is 100% open-source. If you have any doubts, I highly recommend cloning the repository and running the script directly from the source code (Python), allowing you to audit exactly what is being changed on your system.

---

## ⚙️ Core Features

* **🗃️ Portable Safety Backup:** Automatically creates a `.reg` file backup in the local directory before applying any modifications, ensuring safe recovery.
* **⚡ Network Throttling Control:** Disables Windows' network packet throttling mechanism, adjusting system responsiveness for perfect audio and network stability.
* **🎯 Nagle's Algorithm Optimization:** Adjusts `TCPNoDelay` and `TcpAckFrequency` parameters across active network interfaces to send packets immediately, drastically reducing in-game ping.
* **🌐 TCP Stack Stabilization:** Optimizes Windows stack features like *Receive Side Scaling (RSS)*, while ensuring maximum compatibility with online games by disabling unstable experimental features like *TCP Fast Open (TFO)*.
* **📏 Dynamic MTU Discovery:** Performs an active ping-based diagnostic scan to discover and safely apply the optimal *Maximum Transmission Unit* (MTU) size, effectively eliminating packet fragmentation.
* **🔍 Performance DNS Switch:** Provides a quick and secure configuration for the world's fastest public DNS servers (Google DNS and Cloudflare DNS).

---

## 🛠️ How to Use

### 🐍 Option 1: Via Python (Recommended for Developers)
This option allows you to audit the code in real-time.

1. **Install Python 3.x** from [python.org](https://www.python.org/).
2. Clone the repository:
   `git clone https://github.com/wictorfeitosa/internet-optimizer.git`
3. Enter the folder:
   `cd internet-optimizer`
4. Run the main script:
   `python internet_optimizer.py`
   *(The script will detect the need for elevated privileges and automatically request Administrator permission).*

### 💻 Option 2: Via Executable (.exe)
Ideal for end-users.

1. Download the `internet_optimizer.exe` file from the **Releases** section.
2. **Right-click** the file and select **"Run as administrator"**.
3. The tool will automatically detect your network interfaces, perform MTU tests, and apply the optimal stability configuration.

---

## 🏗️ Developer's Guide (How to generate the .exe)

If you have modified the source code and need to generate a new executable:

1. Ensure you have **Python** installed.
2. Install PyInstaller: `pip install pyinstaller`
3. Generate the binary in the root folder:
   `pyinstaller --onefile --icon=moose.ico internet_optimizer.py`
4. Your executable will be in the `dist/` folder.

---

## 🛠️ Tech Stack & Authorship

* **Core Engine:** Built in **Python 3** using `ctypes`, `winreg`, and `subprocess`.
* **Interface:** Interactive **Command Line Interface (CLI)** with ANSI color rendering.
* **Development:** Concept, supervision, and environment testing conducted by **Wictor Feitosa**.

---

## 📜 License

This project is distributed under the **MIT License**. You are free to use, modify, and distribute it, provided that the original credits are maintained.
