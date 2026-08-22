# Quarky Intellio Python UDP Controller

A lightweight Python script designed to communicate directly with the **STEMpedia Quarky Intellio** robot over a local Wi-Fi network using standard UDP sockets. 

This project accompanies the tutorial on network packet analysis, reverse engineering, and ethical hacking for educational robotics.

---

## 🚀 Overview

While the Quarky Intellio is natively programmed using PictoBlox, advanced students can explore the underlying network communication layer. By capturing Wi-Fi packets via tools like Wireshark, we can isolate the UDP control payloads and replicate them programmatically using Python.

This script acts as a custom client that sends raw command payloads directly to the robot's IP address, bypassing the official software environment for pure learning purposes in networking, IoT protocols, and automation.

---

## 🛠️ Prerequisites

* Python 3.x installed on your machine.
* A computer and your Quarky Intellio connected to the **same local Wi-Fi network/router**.
* The local IP address of your Quarky Intellio.

---

## ⚙️ Configuration

Open the script (`main.py` or `controller.py`) and update the configuration variables to match your network setup:

```python
# Configuration
TARGET_IP = "192.168.29.24"  # Replace with your Quarky Intellio's IP address
TARGET_PORT = 5006           # Default communication port
PAYLOAD = "frame/2/202/8/1"  # The isolated command payload string
```

---

## 💻 Code

```python
import socket

# Configuration
TARGET_IP = "192.168.29.24"
TARGET_PORT = 5006
# The extracted data payload from the capture
PAYLOAD = "frame/2/202/8/1"

def send_udp_payload():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Encode string to bytes
    sock.sendto(PAYLOAD.encode('utf-8'), (TARGET_IP, TARGET_PORT))
    print(f"Payload sent to {TARGET_IP}:{TARGET_PORT}")

if __name__ == "__main__":
    send_udp_payload()
```

---

## ▶️ Usage

1. Turn on your Quarky Intellio and connect it to your Wi-Fi network to obtain its IP address.
2. Ensure your computer is connected to the same network.
3. Run the script from your terminal:

```bash
python controller.py
```

---

## 🎥 Watch the Tutorial

For a complete step-by-step walkthrough on how to use Wireshark to sniff packets, isolate the data payload, and execute this code, check out the video tutorial:

👉 **[Watch on YouTube](https://www.youtube.com/watch?v=6j_3CEHQ6u0)**

---

## ⚠️ Disclaimer

This project is created strictly for **educational and ethical hacking learning purposes** for higher-grade students and educators. A huge shoutout to **STEMpedia** for creating such an open, versatile hardware platform that encourages deep exploration into IoT and networking!
