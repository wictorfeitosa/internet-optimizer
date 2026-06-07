# 🚀 Internet Optimizer

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.2.1-orange)

A high-performance utility designed to optimize Windows network settings, reducing **latency (ping)** and improving connection stability for gaming and real-time applications.

---

## 🛡️ Transparency and Security

> [!IMPORTANT]
> This software performs low-level modifications to the **Windows Registry** and utilizes network commands (`netsh`). For these reasons, **Windows Defender** or third-party antivirus software may flag the executable file as "suspicious."

**This behavior is a common false positive.** The code is 100% open-source and fully auditable.

---

## ⚙️ Core Features (v1.2.1)

* **🗃️ Portable Safety Backup:** Automatically creates a `.reg` file backup before applying any modifications.
* **⚡ Network Throttling Control:** Disables Windows' network packet throttling for maximum system responsiveness.
* **🎯 Nagle's Algorithm Optimization:** Configures TCP parameters for immediate packet delivery.
* **🌐 TCP Stack Stabilization:** Optimizes stack features (RSS) while enforcing strict compatibility (disabling *Fast Open* and *ECN*) to prevent session drops in online games.
* **📏 Dynamic MTU Discovery:** Executes an active diagnostic scan to determine your connection's true MTU limit, eliminating packet fragmentation.
* **🔄 Automated Network Reset:** The script now automatically performs a complete socket, cache, and DNS cleanup (`flushdns`, `winsock reset`, `ip reset`) for a "clean slate" network state.

---

## 🛠️ How to Use

### 🐍 Option 1: Via Python
Run: `python internet_optimizer.py`

### 💻 Option 2: Via Executable (.exe)
| 📥 QUICK DOWNLOAD |
| :--- |
| **[👉 Click here to download internet_optimizer.exe](https://github.com/wictorfeitosa/internet-optimizer/releases/download/v1.2.1/internet_optimizer.exe)** |

1. Download the `internet_optimizer.exe` file.
2. **Right-click** the file and select **"Run as administrator"**.
3. Follow the terminal instructions. **A system reboot is required** after completion to finalize the network stack reset.

---

## 📜 License

This project is distributed under the **MIT License**.
