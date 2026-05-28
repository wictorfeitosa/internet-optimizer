# 🚀 Internet Optimizer

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=blue)
![License](https://img.shields.io/badge/License-MIT-green)

A high-performance utility designed to optimize Windows network settings, reducing **latency (ping)** and improving connection stability for gaming and real-time applications.

---

## 🛡️ Transparency and Security

> [!IMPORTANT]
> This software performs low-level modifications to the **Windows Registry** and utilizes network commands (`netsh`). For these reasons, **Windows Defender** or third-party antivirus software may flag the executable file as "suspicious."

**This behavior is a common false positive in optimization tools.** The code is 100% open-source. If you have any doubts or hesitation about running the executable, I highly recommend cloning this repository and running the script directly from the source code (Python), allowing you to audit exactly what is being changed on your machine before applying it.

---

## 📦 Note on the Executable (.exe)

For the end user to run the optimizer with just two clicks (without needing to install Python), **the executable file must be generated beforehand.** The process works as follows:
1. The developer writes the code in Python (`internet_optimizer.py` and `utils.py`).
2. The developer uses the `PyInstaller` tool to compile and package this code.
3. `PyInstaller` bundles the source code and an embedded Python interpreter into a single standalone `.exe` file.
4. This final file is made available in the **Releases** section for standard users.

---

## ⚙️ Core Features

* **🗃️ Portable Safety Backup:** Automatically creates a `.reg` file inside the script's local directory before making any modifications, ensuring safe recovery and maximum portability across systems without hardcoded drive dependencies.
* **🧠 Smart Connection Profiling:** Features an interactive menu that detects whether you use **Fiber/Cable** or **Wireless/Radio** links, dynamically selecting the best TCP auto-tuning level (`normal`, `restricted`, or `highlyrestricted`) to prevent bufferbloat and packet loss on unstable signals.
* **⚡ Network Throttling Control:** Disables the network throttling mechanism that Windows imposes on network packets, setting the system responsiveness balance to 15% for perfect background process and audio stability.
* **🎯 Nagle's Algorithm Optimization:** Adjusts `TCPNoDelay` and `TcpAckFrequency` parameters across active network interfaces to send packets immediately, drastically reducing in-game ping.
* **🌐 Advanced TCP Global Tuning:** Activates cutting-edge Windows stack features, including *Receive Side Scaling (RSS)* for multi-core packet distribution and *TCP Fast Open (TFO)* for faster connection handshakes.
* **📏 Dynamic MTU Configuration:** Performs automatic interface scanning to discover and safely apply the ideal Maximum Transmission Unit (MTU) size without causing fragmentations.
* **🔍 Performance DNS Switch:** Provides the option to quickly configure the fastest and most secure public DNS servers globally (Google DNS and Cloudflare DNS).

---

## 🛠️ How to Use

### 🐍 Option 1: Via Python (Recommended for Developers)
This option requires you to have the Python interpreter installed on your machine, allowing you to view and audit the code in real time.

1. **Install Python 3.x** from the official website: [python.org](https://www.python.org/)
2. **Open your terminal** (Command Prompt, PowerShell, or Git Bash) and clone the repository:
   git clone [https://github.com/wictorfeitosa/internet-optimizer.git](https://github.com/wictorfeitosa/internet-optimizer.git)
3. **Navigate to the project folder**:
   cd internet-optimizer
4. **Run the main script**:
   python internet_optimizer.py
   *(The script will detect the need for elevated privileges and automatically request to run as Administrator).*

### 💻 Option 2: Via Executable (.exe)
Ideal for end users who do not have or do not wish to install Python on their computer.

1. Head over to the **Releases** tab of this repository and download the `internet_optimizer.exe` file.
2. **Right-click** the downloaded file and select **"Run as administrator"**.
3. Answer the interactive terminal questions regarding your connection type (Fiber vs. Radio) and speed to apply the customized profile.

---

## 🏗️ Developer's Guide (How to Generate the .exe)

To keep the project professional and aligned with Software Engineering best practices, the code architecture is broken down modularly (`utils.py` and `internet_optimizer.py`).

If you have modified the source code and need to **generate or update the executable**, follow the step-by-step instructions below:

1. **Prerequisite:** Make sure you have **Python** installed on your development machine.
2. Install PyInstaller using Python's package manager:
   pip install pyinstaller
3. Generate the standalone compressed binary by running the following command in the root folder of the project:
   pyinstaller --onefile --icon=moose.ico internet_optimizer.py
4. Your freshly compiled executable file will be generated cleanly inside an automatically created directory named `dist/`. Simply grab the `internet_optimizer.exe` file from there.

---

## 🛠️ Tech Stack & Authorship

* **Core Engine:** Built entirely in **Python 3** utilizing native `ctypes`, `winreg`, and `subprocess`.
* **Interface:** Powered by an interactive, customized **Command Line Interface (CLI)** with native ANSI color rendering on Windows terminal environments.
* **Development & Testing:** Concept, supervision, and end-to-end environment testing strictly conducted by **Wictor Feitosa**.

---

## 📜 License

This project is distributed under the **MIT License**. This means you are completely free to use, modify, study, and distribute the code, provided that the original developer credits are maintained.
