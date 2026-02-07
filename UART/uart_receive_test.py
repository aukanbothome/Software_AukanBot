"""
uart_receive_test.py
Lee continuamente del puerto UART y muestra todo lo que envía el ESP32.
Útil para depuración del protocolo.
"""

import serial
import time

UART_PORT = "/dev/serial0"
UART_BAUDRATE = 115200
UART_TIMEOUT = 1.0

def main():
    print(f"[UART_RX] Escuchando en {UART_PORT} a {UART_BAUDRATE} baudios...")
    ser = serial.Serial(UART_PORT, UART_BAUDRATE, timeout=UART_TIMEOUT)
    time.sleep(2)

    try:
        while True:
            if ser.in_waiting:
                linea = ser.readline().decode("utf-8", errors="ignore").strip()
                if linea:
                    print("[UART_RX] <-", linea)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\n[UART_RX] Salida por teclado.")
    finally:
        ser.close()
        print("[UART_RX] Puerto cerrado.")


if __name__ == "__main__":
    main()
