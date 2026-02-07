# MÁQUINA DE ESTADOS FINITOS – Prueba3
# Recepción de Invitados
# Cada estado representa una acción del robot
# durante la recepción de personas.


def estado_inicio():
    print("Q1: Robot en el punto inicial")
    while True:
        evento = yield
        if evento == 'a':
            yield from estado_inicio()
        elif evento == 'b':
            yield from estado_detectar_invitado()
        else:
            break


def estado_detectar_invitado():
    print("Q2: Detectando la llegada del invitado")
    while True:
        evento = yield
        if evento == 'c':
            yield from estado_preguntas_iniciales()
        else:
            break


def estado_preguntas_iniciales():
    print("Q3: Realizando preguntas iniciales")
    while True:
        evento = yield
        if evento == 'd':
            yield from estado_guiar_bebidas()
        else:
            break


def estado_guiar_bebidas():
    print("Q4: Guiando al invitado al área de bebidas")
    while True:
        evento = yield
        if evento == 'e':
            yield from estado_mostrar_bebidas()
        elif evento == 'f':
            yield from estado_obstaculo()
        elif evento == 'g':
            yield from estado_invitado_perdido()
        else:
            break


def estado_mostrar_bebidas():
    print("Q5: Mostrando bebidas disponibles")
    while True:
        evento = yield
        if evento == 'h':
            yield from estado_identificar_bebida()
        else:
            break


def estado_identificar_bebida():
    print("Q6: Identificando bebida elegida")
    while True:
        evento = yield
        if evento == 'i':
            yield from estado_guiar_sala()
        elif evento == 'j':
            yield from estado_invitado_perdido()
        else:
            break


def estado_guiar_sala():
    print("Q7: Guiando al invitado a la sala")
    while True:
        evento = yield
        if evento == 'u':
            yield from estado_asignar_asiento()
        elif evento == 'k':
            yield from estado_obstaculo()
        else:
            break


def estado_asignar_asiento():
    print("Q8: Indicando asiento asignado")
    while True:
        evento = yield
        if evento == 'l':
            yield from estado_presentar_invitados()
        else:
            break


def estado_presentar_invitados():
    print("Q9: Presentando al invitado con otros")
    while True:
        evento = yield
        if evento == 'm':
            yield from estado_esperar_siguiente()
        else:
            break


def estado_esperar_siguiente():
    print("Q10: Esperando al siguiente invitado")
    while True:
        evento = yield
        if evento == 'n':
            yield from estado_detectar_invitado()
        elif evento == 'w':
            yield from estado_esperar_siguiente()
        else:
            break


def estado_obstaculo():
    print("Q11: Obstáculo detectado")
    while True:
        evento = yield
        if evento == 'p':
            yield from estado_guiar_bebidas()
        elif evento == 'q':
            yield from estado_guiar_sala()
        elif evento == 'o':
            yield from estado_obstaculo()
        else:
            break


def estado_invitado_perdido():
    print("Q12: Manejando invitado perdido")
    while True:
        evento = yield
        if evento == 's':
            yield from estado_detectar_invitado()
        elif evento == 'r':
            yield from estado_invitado_perdido()
        else:
            break


# ==============================
# CONTROLADOR FSM
# ==============================
def ejecutar_fsm():
    estado_actual = estado_inicio()
    next(estado_actual)

    while True:
        try:
            entrada = input("Ingresa una tecla (a–w) o 'exit': ").lower()
            if entrada == "exit":
                print("FSM finalizada.")
                break

            estado_actual.send(entrada)

        except StopIteration:
            print("Estado final o transición inválida.")
            break


if __name__ == "__main__":
    ejecutar_fsm()

#In English

# FINITE STATE MACHINE TEST3
# Guest Reception Task
# Each state represents a behavior of the robot
# during the guest reception process.


def state_start():
    print("Q1: Robot at starting point")
    while True:
        event = yield
        if event == 'a':
            yield from state_start()
        elif event == 'b':
            yield from state_detect_guest()
        else:
            break


def state_detect_guest():
    print("Q2: Detecting guest appearance")
    while True:
        event = yield
        if event == 'c':
            yield from state_initial_questions()
        else:
            break


def state_initial_questions():
    print("Q3: Asking initial questions to the guest")
    while True:
        event = yield
        if event == 'd':
            yield from state_guide_to_drinks()
        else:
            break


def state_guide_to_drinks():
    print("Q4: Guiding guest to drinks area")
    while True:
        event = yield
        if event == 'e':
            yield from state_show_drinks()
        elif event == 'f':
            yield from state_obstacle()
        elif event == 'g':
            yield from state_lost_guest()
        else:
            break


def state_show_drinks():
    print("Q5: Showing available drinks")
    while True:
        event = yield
        if event == 'h':
            yield from state_identify_drink()
        else:
            break


def state_identify_drink():
    print("Q6: Identifying chosen drink")
    while True:
        event = yield
        if event == 'i':
            yield from state_guide_living_room()
        elif event == 'j':
            yield from state_lost_guest()
        else:
            break


def state_guide_living_room():
    print("Q7: Guiding guest to living room")
    while True:
        event = yield
        if event == 'u':
            yield from state_assign_seat()
        elif event == 'k':
            yield from state_obstacle()
        else:
            break


def state_assign_seat():
    print("Q8: Indicating assigned seat")
    while True:
        event = yield
        if event == 'l':
            yield from state_introduce_guests()
        else:
            break


def state_introduce_guests():
    print("Q9: Introducing guest to others")
    while True:
        event = yield
        if event == 'm':
            yield from state_wait_next_guest()
        else:
            break


def state_wait_next_guest():
    print("Q10: Waiting for the next guest")
    while True:
        event = yield
        if event == 'n':
            yield from state_detect_guest()
        elif event == 'w':
            yield from state_wait_next_guest()
        else:
            break


def state_obstacle():
    print("Q11: Obstacle detected")
    while True:
        event = yield
        if event == 'p':
            yield from state_guide_to_drinks()
        elif event == 'q':
            yield from state_guide_living_room()
        elif event == 'o':
            yield from state_obstacle()
        else:
            break


def state_lost_guest():
    print("Q12: Handling lost guest situation")
    while True:
        event = yield
        if event == 's':
            yield from state_detect_guest()
        elif event == 'r':
            yield from state_lost_guest()
        else:
            break

# FSM CONTROLLER
def run_fsm():
    current_state = state_start()
    next(current_state)

    while True:
        try:
            user_input = input("Enter a key (a–w) or 'exit': ").lower()
            if user_input == "exit":
                print("FSM execution finished.")
                break

            current_state.send(user_input)

        except StopIteration:
            print("Final state reached or invalid transition.")
            break


if __name__ == "__main__":
    run_fsm()
