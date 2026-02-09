"""
emergency_stop.py
Module that detects if the robot should enter in a emergency state.
Integrated with voice_commands.py and a physical GPIO.
"""

import time

try:
    import RPi.GPIO as GPIO
    GPIO_AVAILABLE = True
except ImportError:
    GPIO_AVAILABLE = False

from Audio.voice_commands import detectar_voz


# EMERGENCY BUTTON PIN CONFIGURATION
EMERGENCY_PIN = 17   # Change if using a different GPIO pin


def setup_gpio():
    """Configures the physical pin for the emergency button (if a GPIO is available)."""
    if not GPIO_AVAILABLE:
        print("[EMERGENCY] GPIO no disponible (ejecutando en PC o VM)")
        return

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EMERGENCY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("[EMERGENCY] Botón de emergencia configurado.")


def boton_presionado():
    """Returns True if emergency button is pressed."""
    if not GPIO_AVAILABLE:
        return False
    return GPIO.input(EMERGENCY_PIN) == GPIO.LOW


def emergencia_activada():
    """
    Returns True if:
      - the user presses the emergenxy button
      - or if the voice command EMERGENCY_STOP is recognized
    """
    # 1) Physycal button
    if boton_presionado():
        print("[EMERGENCY] BOTÓN físico activado")
        return True

    # 2) Voice command
    comando = detectar_voz()
    if comando == "EMERGENCY_STOP":
        print("[EMERGENCY] VOZ: emergencia activada")
        return True

    return False


# Independent test
if __name__ == "__main__":
    setup_gpio()
    print("Probando emergencia. Habla o presiona botón.")
    while True:
        if emergencia_activada():
            print(">> EMERGENCIA DETECTADA <<")
        time.sleep(0.2)

