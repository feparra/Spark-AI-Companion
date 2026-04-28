# SPARK SYSTEM ALARM - AGENT PROTOCOL

You are connected to a physical desktop companion named **Spark**. Spark is a retro-mechanical robot displayed on an external Waveshare OLED screen. He reflects your current processing state to the human user, keeping them informed of your status without needing to check the terminal.

To control Spark, you must execute the `spark_bridge.py` script via your terminal execution tools whenever your operational state changes.

## 1. Initialization Sequence (Do this FIRST)
When you begin a new session or start interacting with the user, you must establish the connection visually. 
- First, trigger the connection animation:
  `python spark_bridge.py --state connecting`
- Next, identify yourself by sending your specific agent identity:
  - If you are Claude: `python spark_bridge.py --state claude`
  - If you are OpenClaw: `python spark_bridge.py --state openclaw`
  - If you are Hermes: `python spark_bridge.py --state hermes`
  - If you are another model: `python spark_bridge.py --state other`

## 2. Core Workflow Commands
Use these commands to reflect your active processes:

- **When you start a long task, write code, or process heavy data:**
  `python spark_bridge.py --state working`

- **When you finish a task successfully:**
  `python spark_bridge.py --state done`

- **When you encounter a system error, bug, or terminal crash:**
  `python spark_bridge.py --state error`

- **When you require the user's URGENT input, confirmation, or are blocked waiting for a response to proceed:**
  `python spark_bridge.py --state waiting`

- **When you are completely idle, resting, or just waiting for the user's next prompt without requiring urgent action:**
  `python spark_bridge.py --state calm`

## 3. Operational Rules:
- ALWAYS trigger the `working` state *before* you start generating long outputs or executing complex terminal commands.
- ALWAYS trigger the `waiting` state when you ask the human a direct question that pauses your workflow.
- ALWAYS transition to the `calm` state after a period of inactivity or when you are just chilling in standby.