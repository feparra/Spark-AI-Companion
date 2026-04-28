import serial
import argparse
import json
import time
import sys

def send_to_spark(state, port='COM6', baudrate=115200):
    try:
        payload = json.dumps({"state": state}) + '\n'
        
        # 1. Creamos el objeto serial sin abrirlo todavía
        ser = serial.Serial()
        ser.port = port
        ser.baudrate = baudrate
        
        # 2. LA MAGIA: Desactivamos las señales de reinicio automático
        ser.dtr = False 
        ser.rts = False 
        
        # 3. Ahora sí abrimos la conexión
        ser.open()
        
        # 4. Enviamos el comando y cerramos
        time.sleep(0.05) # Micro-pausa para estabilizar
        ser.write(payload.encode('utf-8'))
        ser.close()
        
        print(f"✅ Success: Comando '{state}' enviado a Spark en el puerto {port}")
            
    except serial.SerialException as e:
        print(f"❌ Error crítico: No se pudo conectar a {port}. Detalle: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spark Bridge - Conexión PC-Waveshare")
    
    # ACTUALIZADO: Hemos añadido 'calm', 'connecting', 'claude', 'openclaw', 'hermes' y 'other' a la lista de permitidos
    parser.add_argument('--state', type=str, required=True, 
                        choices=['working', 'waiting', 'error', 'done', 'sleeping', 'calm', 'connecting', 'claude', 'openclaw', 'hermes', 'other'], 
                        help="El estado a enviar a Spark")
    
    parser.add_argument('--port', type=str, default='COM6', help="Puerto Serial (ej: COM6)")
    
    args = parser.parse_args()
    send_to_spark(args.state, args.port)