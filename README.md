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