"""
robot_state_machine.py
Main state machine for the RobotCup's robot.
Uses information from Vision + UART + Audio + Emergency Stop.
"""

from enum import Enum, auto
import time
import numpy as np

from UART.uart_send import UartRobot
from Audio.text_to_speech import hablar
from Logic.emergency_stop import emergencia_activada

# =====================
#  ROBOT STATES
# =====================
class Estado(Enum):
    INIT = auto()
    BUSCANDO_PERSONA = auto()
    APROXIMANDO_PERSONA = auto()
    DISTANCIA_SEGURA = auto()
    EMERGENCIA = auto()


# =====================
#  GLOBAL PARAMETERS
# =====================
SAFE_DISTANCE = 1.2     # minimum safe distance
LOST_TIMEOUT = 2        # timeout (seconds) before the user is considered lost


# =====================
#  VISION FUNCTIONING
# =====================

def obtener_pose_robot():
    """
    Returns (Xr, Zr) in meters.
    This function must connect to slam_person_map.py.
    For now, it returns a static example.
    """
    # connect ALL to cam_pose from SLAM
    return 0.0, 0.0


def obtener_persona_en_mapa():
    """
    Returns:
      - None if no person is detected
      - or (Xp, Zp, dist)
      
    Where dist is the actual distance between the person and the robot.
    """
    # connect ALL to slam_person_map.py
    return None


# =====================
#  STATE MACHINE
# =====================

def main():
    estado = Estado.INIT
    uart = UartRobot()

    ultima_vista = 0
    objetivo = None

    hablar("Sistema iniciado. Preparando sensores.")

    while True:

        # --- EMERGENCY DETECTION ---
        if emergencia_activada():
            estado = Estado.EMERGENCIA

        # --- UPDATE USER PERCEPTION ---
        Xr, Zr = obtener_pose_robot()
        persona = obtener_persona_en_mapa()
        ahora = time.time()

        if persona:
            Xp, Zp, dist = persona
            ultima_vista = ahora
        else:
            dist = None

        # --- FSM PROCESSING ---
        if estado == Estado.INIT:
            print("[FSM] INIT")
            uart.send("STOP_BASE")
            hablar("Sensores listos. Iniciando búsqueda de personas.")
            estado = Estado.BUSCANDO_PERSONA

        elif estado == Estado.BUSCANDO_PERSONA:
            print("[FSM] BUSCANDO_PERSONA")

            uart.send("BASE_EXPLORAR")

            if persona is not None:
                # Safe target calculations
                vx = Xp - Xr
                vz = Zp - Zr
                norm = np.sqrt(vx*vx + vz*vz) + 1e-6

                X_target = Xp - SAFE_DISTANCE * (vx / norm)
                Z_target = Zp - SAFE_DISTANCE * (vz / norm)
                objetivo = (X_target, Z_target)

                hablar("Persona detectada. Aproximando.")
                estado = Estado.APROXIMANDO_PERSONA

        elif estado == Estado.APROXIMANDO_PERSONA:
            print("[FSM] APROXIMANDO_PERSONA")

            if persona is None and (ahora - ultima_vista) > LOST_TIMEOUT:
                hablar("Persona perdida. Reanudando búsqueda.")
                estado = Estado.BUSCANDO_PERSONA
                continue

            Xt, Zt = objetivo
            ex = Xt - Xr
            ez = Zt - Zr
            dist_obj = np.sqrt(ex*ex + ez*ez)

            if dist is not None and dist <= SAFE_DISTANCE:
                uart.send("STOP_BASE")
                hablar("Distancia segura alcanzada.")
                estado = Estado.DISTANCIA_SEGURA
            else:
                uart.send(f"BASE_GOTO:{Xt:.2f},{Zt:.2f}")

        elif estado == Estado.DISTANCIA_SEGURA:
            print("[FSM] DISTANCIA_SEGURA")

            uart.send("STOP_BASE")
            uart.send("SALUDAR")
            hablar("Hola. Mantendré una distancia segura.")

            # Return to search if the person is no longer detected
            if persona is None and (ahora - ultima_vista) > LOST_TIMEOUT:
                hablar("Persona perdida. Reanudando búsqueda.")
                estado = Estado.BUSCANDO_PERSONA

        elif estado == Estado.EMERGENCIA:
            print("[FSM] EMERGENCIA")
            uart.send("STOP_BASE")
            uart.send("STOP_BRAZOS")
            hablar("Parada de emergencia activada.")
            time.sleep(0.2)
            continue  # Keep loop

        time.sleep(0.1)


if __name__ == "__main__":
    main()

