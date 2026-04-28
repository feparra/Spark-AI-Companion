# 🤖 Spark - The Physical AI Companion

Spark is a physical, retro-mechanical desktop robot that lives on a Waveshare OLED screen. He connects to your local AI agents (like OpenClaw, Claude Code, or Cursor) and physically reacts to what the AI is doing in real-time (working, waiting, errors, etc.).

## 🚀 How to Install (For Humans)
If you want your AI Agent to use Spark, simply tell your agent to install it! 

Copy and paste this prompt to your Agent:
> *"Please clone the repository `https://github.com/feparra/Spark-AI-Companion.git`, install the dependencies from `requirements.txt`, and read the `AGENT_GUIDE.md` to learn how to communicate with my desktop robot."*

## 🛠️ Manual Installation
1. Clone this repository: `git clone https://github.com/feparra/Spark-AI-Companion.git `
2. Install dependencies: `pip install -r requirements.txt`
3. Include the rules from `AGENT_GUIDE.md` into your agent's system prompt or context.
4. Test the connection: `python spark_bridge.py --state connecting --port COM6`

## ⚙️ Requirements
- Python 3.8+
- An ESP32-S3 Waveshare Screen running the Spark Firmware.

opia este bloque para tu GitHub (Puedes agregarlo al final del README.md):
Markdown
## 🐧 Linux & WSL2 Troubleshooting Guide

If you are running your AI Agent inside **WSL2 (Ubuntu on Windows)** or a native Linux environment, you might run into some strict OS-level security and hardware rules. Here is how to fix the most common issues:

### 1. WSL2 cannot see the USB Port (Device not found)
By default, WSL2 acts as a virtual machine and cannot directly see Windows USB devices. You must "forward" the USB connection from Windows to Ubuntu.

**Solution (Using `usbipd-win`):**
1. Open **Windows PowerShell as Administrator** and install the USBIPD tool:
   ```powershell
   winget install --interactive --exact dorssel.usbipd-win
(Close and reopen PowerShell as Administrator after installation).
2. List your connected USB devices to find Spark's BUSID (e.g., 1-2 or 2-1):

PowerShell
usbipd list
Bind and attach the device to WSL (replace 1-2 with your actual BUSID):

PowerShell
usbipd bind --busid 1-2
usbipd attach --wsl --busid 1-2
Verify in your Ubuntu Terminal:

Bash
ls /dev/ttyACM*
# or
ls /dev/ttyUSB*
If you see /dev/ttyACM0 or similar, the connection is successful!

2. "Permission Denied" Error in Linux
Unlike Windows, Linux requires explicit user permissions to read or write to serial hardware ports.

Solution:
Grant read/write access to the specific port by running this command in your Linux terminal (replace /dev/ttyACM0 if your port is different):

Bash
sudo chmod a+rw /dev/ttyACM0
3. "python: command not found"
Modern Ubuntu/Linux distributions do not map the python command by default to avoid conflicts with older versions.

Solution:
You must use python3 instead. Make sure to instruct your AI Agent:

"Since we are on Ubuntu, you MUST use python3 spark_bridge.py --state <state> instead of python."

⚙️ Note on Linux Auto-Reboot Behavior
Opening a serial port in Linux inherently forces an ESP32 microcontroller to reboot. Our spark_bridge.py script is smart enough to detect the Operating System. If it detects Linux, it will automatically pause for 3 seconds to let Spark finish its boot sequence before sending the payload. No action is required from you, but expect a slight delay compared to the instantaneous Windows experience!