
# MAQUINA DE ESTADOS DEL ROBOT PRUEBA 1

# Cada función representa un estado.
# Las transiciones dependen del carácter recibido con send().


def estado_espera():
    print("Estado Q1: Esperando a la persona")
    while True:
        evento = yield
        if evento == 'a':
            yield from estado_espera()
        elif evento == 'b':
            yield from estado_preparado()
        else:
            break


def estado_preparado():
    print("Estado Q2: Indicando que el robot está listo")
    while True:
        evento = yield
        if evento == 'c':
            yield from estado_espera()
        elif evento == 'd':
            yield from estado_seguimiento()
        else:
            break


def estado_seguimiento():
    print("Estado Q3: Siguiendo a la persona")
    while True:
        evento = yield
        if evento == 'g':
            yield from estado_deteccion()
        elif evento == 'f':
            yield from estado_seguimiento()
        else:
            break


def estado_deteccion():
    print("Estado Q4: Persona detenida / Detectando indicación")
    while True:
        evento = yield
        if evento == 'h':
            yield from estado_seguimiento()
        elif evento == 'i':
            yield from estado_detectar_bolso()
        elif evento == 'e':
            yield from estado_espera()
        else:
            break


def estado_detectar_bolso():
    print("Estado Q5: Reconociendo el bolso")
    while True:
        evento = yield
        if evento == 'k':
            yield from estado_ir_bolso()
        elif evento == 'j':
            yield from estado_deteccion()
        else:
            break


def estado_ir_bolso():
    print("Estado Q6: Navegando hacia el bolso")
    while True:
        evento = yield
        if evento == 'l':
            yield from estado_tomar_bolso()
        else:
            break


def estado_tomar_bolso():
    print("Estado Q7: Tomando el bolso")
    while True:
        evento = yield
        if evento == 'm':
            yield from estado_regreso()
        else:
            break


def estado_regreso():
    print("Estado Q8: Regresando al punto inicial")
    while True:
        evento = yield
        if evento == 'o':
            yield from estado_obstaculos()
        elif evento == 'n':
            yield from estado_entrega()
        else:
            break


def estado_obstaculos():
    print("Estado Q9: Detectando obstáculos")
    while True:
        evento = yield
        if evento == 'p':
            yield from estado_regreso()
        else:
            break


def estado_entrega():
    print("Estado Q10: Entregando el bolso")
    while True:
        evento = yield
        if evento == 'q':
            yield from estado_fila()
        else:
            break


def estado_fila():
    print("Estado Q11: En espera final (fila)")
    while True:
        evento = yield
        if evento == 'r':
            yield from estado_espera()
        else:
            break


# ==============================
# CONTROLADOR PRINCIPAL
# ==============================
def ejecutar_fsm():
    estado_actual = estado_espera()
    next(estado_actual)  # Inicializa el generador

    while True:
        try:
            entrada = input("Ingresa una letra (a–r) o 'exit': ").lower()
            if entrada == "exit":
                print("FSM finalizada.")
                break

            estado_actual.send(entrada)

        except StopIteration:
            print("Estado final alcanzado o transición inválida.")
            break


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_fsm()

# IN ENGLISH

# ROBOT FINITE STATE MACHINE TEST1

# Each function represents a state.
# Transitions depend on the character received via send().


def state_waiting():
    print("State Q1: Waiting for the person")
    while True:
        event = yield
        if event == 'a':
            yield from state_waiting()
        elif event == 'b':
            yield from state_ready()
        else:
            break


def state_ready():
    print("State Q2: Indicating robot readiness")
    while True:
        event = yield
        if event == 'c':
            yield from state_waiting()
        elif event == 'd':
            yield from state_following()
        else:
            break


def state_following():
    print("State Q3: Following the person")
    while True:
        event = yield
        if event == 'g':
            yield from state_detection()
        elif event == 'f':
            yield from state_following()
        else:
            break


def state_detection():
    print("State Q4: Person stopped / Detecting indication")
    while True:
        event = yield
        if event == 'h':
            yield from state_following()
        elif event == 'i':
            yield from state_bag_recognition()
        elif event == 'e':
            yield from state_waiting()
        else:
            break


def state_bag_recognition():
    print("State Q5: Recognizing the bag")
    while True:
        event = yield
        if event == 'k':
            yield from state_move_to_bag()
        elif event == 'j':
            yield from state_detection()
        else:
            break


def state_move_to_bag():
    print("State Q6: Navigating to the bag")
    while True:
        event = yield
        if event == 'l':
            yield from state_pick_bag()
        else:
            break


def state_pick_bag():
    print("State Q7: Picking up the bag")
    while True:
        event = yield
        if event == 'm':
            yield from state_return_home()
        else:
            break


def state_return_home():
    print("State Q8: Returning to home position")
    while True:
        event = yield
        if event == 'o':
            yield from state_obstacle_detection()
        elif event == 'n':
            yield from state_delivery()
        else:
            break


def state_obstacle_detection():
    print("State Q9: Detecting obstacles")
    while True:
        event = yield
        if event == 'p':
            yield from state_return_home()
        else:
            break


def state_delivery():
    print("State Q10: Delivering the bag")
    while True:
        event = yield
        if event == 'q':
            yield from state_queue()
        else:
            break


def state_queue():
    print("State Q11: Queueing / Final waiting state")
    while True:
        event = yield
        if event == 'r':
            yield from state_waiting()
        else:
            break

# MAIN CONTROLLER
def run_fsm():
    current_state = state_waiting()
    next(current_state)  # Initialize generator

    while True:
        try:
            user_input = input("Enter a key (a–r) or 'exit': ").lower()
            if user_input == "exit":
                print("FSM terminated.")
                break

            current_state.send(user_input)

        except StopIteration:
            print("Final state reached or invalid transition.")
            break


# Program entry point
if __name__ == "__main__":
    run_fsm()
