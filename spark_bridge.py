import serial
import serial.tools.list_ports
import argparse
import json
import time
import sys
import platform # <-- New library to detect the Operating System

def find_spark_port():
    """Scans USB ports to automatically find Spark (ESP32)"""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Look for matches in the description or device name (e.g., /dev/ttyACM0)
        text_to_search = (port.description + " " + port.device).upper()
        if "USB" in text_to_search or "CH340" in text_to_search or "CP210" in text_to_search or "UART" in text_to_search or "ACM" in text_to_search:
            return port.device
    return None

def send_to_spark(state, port='auto', baudrate=115200):
    try:
        # If the port is 'auto', we search for it
        if port == 'auto':
            detected_port = find_spark_port()
            if not detected_port:
                print("❌ Critical Error: No Spark device found connected via USB.")
                sys.exit(1)
            port = detected_port
            print(f"🔍 Spark automatically detected at: {port}")

        payload = json.dumps({"state": state}) + '\n'
        
        ser = serial.Serial()
        ser.port = port
        ser.baudrate = baudrate
        # Disable automatic reset signals (Works mostly on Windows)
        ser.dtr = False 
        ser.rts = False 
        
        ser.open()
        
        # === CROSS-PLATFORM MAGIC ===
        # If we are on Linux/WSL, opening the serial port forces a hardware reboot. 
        # We give it 3 seconds so Spark can finish its delay(2000) and wake up properly.
        if platform.system() == "Linux":
            time.sleep(3.0) 
        else:
            # On Windows there is no reboot, it is almost instantaneous.
            time.sleep(0.05) 
        
        ser.write(payload.encode('utf-8'))
        ser.close()
        
        print(f"✅ Success: Command '{state}' sent to Spark on port {port}")
            
    except serial.SerialException as e:
        print(f"❌ Critical Error: Could not connect to {port}. Detail: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spark Bridge - PC-Waveshare Connection")
    
    parser.add_argument('--state', type=str, required=True, 
                        choices=['working', 'waiting', 'error', 'done', 'sleeping', 'calm', 'connecting', 'claude', 'openclaw', 'hermes', 'other'], 
                        help="The state to send to Spark")
    
    parser.add_argument('--port', type=str, default='auto', help="Serial Port (e.g., COM6 or /dev/ttyACM0). Auto-detects by default.")
    
    args = parser.parse_args()
    send_to_spark(args.state, args.port)