"""
emergency_stop.py
Módulo que detecta si el robot debe entrar en modo de emergencia.
Se integra con voice_commands.py y con un GPIO físico.
"""

import time

try:
    import RPi.GPIO as GPIO
    GPIO_AVAILABLE = True
except ImportError:
    GPIO_AVAILABLE = False

from Audio.voice_commands import detectar_voz


# CONFIGURACIÓN DEL PIN DEL BOTÓN DE EMERGENCIA
EMERGENCY_PIN = 17   # Cambiar si usas otro pin GPIO


def setup_gpio():
    """Configura el pin físico para botón de emergencia (si existe GPIO)."""
    if not GPIO_AVAILABLE:
        print("[EMERGENCY] GPIO no disponible (ejecutando en PC o VM)")
        return

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EMERGENCY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("[EMERGENCY] Botón de emergencia configurado.")


def boton_presionado():
    """Devuelve True si el botón de emergencia está presionado."""
    if not GPIO_AVAILABLE:
        return False
    return GPIO.input(EMERGENCY_PIN) == GPIO.LOW


def emergencia_activada():
    """
    Devuelve True si:
      - el usuario presiona el botón físico
      - o si se reconoce el comando de voz EMERGENCY_STOP
    """
    # 1) Botón físico
    if boton_presionado():
        print("[EMERGENCY] BOTÓN físico activado")
        return True

    # 2) Comando de voz
    comando = detectar_voz()
    if comando == "EMERGENCY_STOP":
        print("[EMERGENCY] VOZ: emergencia activada")
        return True

    return False


# Test independiente
if __name__ == "__main__":
    setup_gpio()
    print("Probando emergencia. Habla o presiona botón.")
    while True:
        if emergencia_activada():
            print(">> EMERGENCIA DETECTADA <<")
        time.sleep(0.2)
