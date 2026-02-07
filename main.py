"""
main.py
Punto de entrada del robot.

Une:
- Vision (detección + SLAM)
- Máquina de estados del robot
- Audio (voz)
- UART (comunicación con ESP32)
- Configuración global
"""

import threading
import time

# ===== IMPORTAR MÓDULOS DEL PROYECTO =====

from Logic.robot_state_machine import main as fsm_main
from Vision.slam_person_map import main as vision_main
from Audio.text_to_speech import hablar

# ===== BANDERAS GLOBALES =====

robot_encendido = True


# ===== HILOS =====

def hilo_vision():
    """
    Hilo dedicado a procesamiento de cámara:
    SLAM + detección de persona + cálculo de posición.
    """
    hablar("Iniciando módulo de visión.")
    try:
        vision_main()
    except Exception as e:
        print("[VISION] ERROR:", e)
        hablar("Error en el módulo de visión.")


def hilo_fsm():
    """
    Máquina de estados principal del robot.
    """
    hablar("Iniciando lógica del robot.")
    try:
        fsm_main()
    except Exception as e:
        print("[FSM] ERROR:", e)
        hablar("Error en la lógica del robot.")


def main():
    """
    Inicializa e inicia todos los módulos del robot.
    """
    hablar("Iniciando sistema RobotCup.")

    # Crear hilos
    t1 = threading.Thread(target=hilo_vision, daemon=True)
    t2 = threading.Thread(target=hilo_fsm, daemon=True)

    # Iniciar hilos
    t1.start()
    t2.start()

    # Mantener vivo el proceso principal
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
