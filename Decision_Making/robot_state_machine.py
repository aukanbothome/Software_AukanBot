"""
robot_state_machine.py
Máquina de estados principal del robot RobotCup.
Usa información de Vision + UART + Audio + Emergency Stop.
"""

from enum import Enum, auto
import time
import numpy as np

from UART.uart_send import UartRobot
from Audio.text_to_speech import hablar
from Logic.emergency_stop import emergencia_activada

# =====================
#  ESTADOS DEL ROBOT
# =====================
class Estado(Enum):
    INIT = auto()
    BUSCANDO_PERSONA = auto()
    APROXIMANDO_PERSONA = auto()
    DISTANCIA_SEGURA = auto()
    EMERGENCIA = auto()


# =====================
#  PARÁMETROS GENERALES
# =====================
SAFE_DISTANCE = 1.2     # distancia mínima segura
LOST_TIMEOUT = 2        # segundos sin ver persona = perdida


# =====================
#  FUNCIONES DE VISIÓN
# =====================

def obtener_pose_robot():
    """
    Devuelve (Xr, Zr) en metros.
    Esta función debe conectarse a slam_person_map.py.
    Por ahora devolvemos un ejemplo fijo.
    """
    # TODO conectar a cam_pose del SLAM
    return 0.0, 0.0


def obtener_persona_en_mapa():
    """
    Debe devolver:
      - None si no hay persona
      - o (Xp, Zp, dist)
    donde dist es la distancia real entre persona y robot.
    """
    # TODO conectar a slam_person_map.py
    return None


# =====================
#  MÁQUINA DE ESTADOS
# =====================

def main():
    estado = Estado.INIT
    uart = UartRobot()

    ultima_vista = 0
    objetivo = None

    hablar("Sistema iniciado. Preparando sensores.")

    while True:

        # --- DETECCIÓN DE EMERGENCIA ---
        if emergencia_activada():
            estado = Estado.EMERGENCIA

        # --- ACTUALIZAR PERCEPCIÓN ---
        Xr, Zr = obtener_pose_robot()
        persona = obtener_persona_en_mapa()
        ahora = time.time()

        if persona:
            Xp, Zp, dist = persona
            ultima_vista = ahora
        else:
            dist = None

        # --- PROCESAR FSM ---
        if estado == Estado.INIT:
            print("[FSM] INIT")
            uart.send("STOP_BASE")
            hablar("Sensores listos. Iniciando búsqueda de personas.")
            estado = Estado.BUSCANDO_PERSONA

        elif estado == Estado.BUSCANDO_PERSONA:
            print("[FSM] BUSCANDO_PERSONA")

            uart.send("BASE_EXPLORAR")

            if persona is not None:
                # Calcular objetivo seguro
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

            # Volver a buscar si la persona se va
            if persona is None and (ahora - ultima_vista) > LOST_TIMEOUT:
                hablar("Persona perdida. Reanudando búsqueda.")
                estado = Estado.BUSCANDO_PERSONA

        elif estado == Estado.EMERGENCIA:
            print("[FSM] EMERGENCIA")
            uart.send("STOP_BASE")
            uart.send("STOP_BRAZOS")
            hablar("Parada de emergencia activada.")
            time.sleep(0.2)
            continue  # no salir del bucle

        time.sleep(0.1)


if __name__ == "__main__":
    main()
