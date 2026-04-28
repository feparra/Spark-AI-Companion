import serial
import serial.tools.list_ports
import argparse
import json
import time
import sys

def find_spark_port():
    """Escanea los puertos USB para encontrar automáticamente a Spark (ESP32)"""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Los chips del ESP32 suelen tener estas palabras en su descripción
        desc = port.description.upper()
        if "USB" in desc or "CH340" in desc or "CP210" in desc or "UART" in desc or "SERIAL" in desc:
            return port.device
    return None

def send_to_spark(state, port='auto', baudrate=115200):
    try:
        # Si el puerto está en 'auto', lo buscamos
        if port == 'auto':
            detected_port = find_spark_port()
            if not detected_port:
                print("❌ Error crítico: No se encontró ningún dispositivo Spark conectado por USB.")
                sys.exit(1)
            port = detected_port
            print(f"🔍 Spark detectado automáticamente en: {port}")

        payload = json.dumps({"state": state}) + '\n'
        
        ser = serial.Serial()
        ser.port = port
        ser.baudrate = baudrate
        ser.dtr = False 
        ser.rts = False 
        
        ser.open()
        time.sleep(0.05)
        ser.write(payload.encode('utf-8'))
        ser.close()
        
        print(f"✅ Success: Comando '{state}' enviado a Spark en el puerto {port}")
            
    except serial.SerialException as e:
        print(f"❌ Error crítico: No se pudo conectar a {port}. Detalle: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spark Bridge - Conexión PC-Waveshare")
    parser.add_argument('--state', type=str, required=True, 
                        choices=['working', 'waiting', 'error', 'done', 'sleeping', 'calm', 'connecting', 'claude', 'openclaw', 'hermes', 'other'], 
                        help="El estado a enviar a Spark")
    
    # Cambiamos el default de 'COM6' a 'auto'
    parser.add_argument('--port', type=str, default='auto', help="Puerto Serial (ej: COM6). Por defecto auto-detecta.")
    
    args = parser.parse_args()
    send_to_spark(args.state, args.port)