"""
uart_send.py
Módulo de ayuda para enviar comandos UART desde la Raspberry Pi
a los ESP32 del robot.
"""

import serial
import time

# Estos valores deberían coincidir con robot_parameters.yaml
UART_PORT = "/dev/serial0"
UART_BAUDRATE = 115200
UART_TIMEOUT = 1.0  # segundos


class UartRobot:
    def __init__(self, port=UART_PORT, baudrate=UART_BAUDRATE, timeout=UART_TIMEOUT):
        print(f"[UART] Abriendo puerto {port} a {baudrate} baudios")
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        time.sleep(2)  # pequeña pausa para que el puerto se estabilice

    def send(self, cmd: str):
        """
        Envía un comando terminado en salto de línea.
        Ej: "STOP_BASE", "BASE_GOTO:1.20,0.50"
        """
        mensaje = cmd.strip() + "\n"
        self.ser.write(mensaje.encode("utf-8"))
        print("[UART] ->", mensaje.strip())

    def close(self):
        self.ser.close()
        print("[UART] Puerto cerrado")


# Test rápido
if __name__ == "__main__":
    uart = UartRobot()
    try:
        while True:
            texto = input("Comando a enviar (ENTER para salir): ").strip()
            if not texto:
                break
            uart.send(texto)
    finally:
        uart.close()
