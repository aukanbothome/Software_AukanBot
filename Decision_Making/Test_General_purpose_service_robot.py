#--------------------------------------------------[ En Español ]--------------------------------------------------

# MÁQUINA DE ESTADOS FINITOS DEL ROBOT PRUEBA2

# Cada estado está representado por un generador.
# Las transiciones dependen del carácter recibido.


def estado_inactivo():
    print("Q1: Robot en estado inactivo")
    while True:
        evento = yield
        if evento == 'a':
            yield from estado_ir_a_mesa()
        else:
            break


def estado_ir_a_mesa():
    print("Q2: Desplazándose hacia la mesa")
    while True:
        evento = yield
        if evento == 'b':
            yield from estado_ir_a_mesa()
        elif evento == 'c':
            yield from estado_observar_mesa()
        elif evento == 'd':
            yield from estado_tomar_objeto()
        elif evento == 'e':
            yield from estado_soltar_objeto()
        else:
            break


def estado_observar_mesa():
    print("Q3: Observando la mesa")
    while True:
        evento = yield
        if evento == 'f':
            yield from estado_clasificar_objeto()
        elif evento == 'g':
            yield from estado_observar_mesa()
        else:
            break


def estado_clasificar_objeto():
    print("Q4: Clasificando el objeto")
    while True:
        evento = yield
        if evento == 't':
            yield from estado_alerta_obstaculo()
        elif evento == 'h':
            yield from estado_ir_a_mesa()
        else:
            break


def estado_tomar_objeto():
    print("Q5: Tomando el objeto")
    while True:
        evento = yield
        if evento == 'i':
            yield from estado_navegar_destino()
        else:
            break


def estado_navegar_destino():
    print("Q6: Navegando hacia el destino")
    while True:
        evento = yield
        if evento == 'j':
            yield from estado_ir_a_mesa()
        elif evento == 's':
            yield from estado_alerta_obstaculo()
        else:
            break


def estado_soltar_objeto():
    print("Q7: Soltando el objeto")
    while True:
        evento = yield
        if evento == 'm':
            yield from estado_verificar_mesa()
        elif evento == 'l':
            yield from estado_soltar_objeto()
        else:
            break


def estado_verificar_mesa():
    print("Q8: Verificando objetos restantes en la mesa")
    while True:
        evento = yield
        if evento == 'n':
            yield from estado_verificar_mesa()
        elif evento == 'o':
            yield from estado_tarea_completada()
        else:
            break


def estado_tarea_completada():
    print("Q9: Tarea completada")
    while True:
        evento = yield
        if evento == 'p':
            yield from estado_detectar_obstaculo()
        else:
            break


def estado_detectar_obstaculo():
    print("Q10: Detectando obstáculo")
    while True:
        evento = yield
        if evento == 'q':
            yield from estado_ir_a_mesa()
        else:
            break


def estado_alerta_obstaculo():
    print("Q11: Obstáculo detectado, esperando resolución")
    while True:
        evento = yield
        if evento == 'r':
            yield from estado_ir_a_mesa()
        else:
            break

# CONTROLADOR PRINCIPAL

def ejecutar_fsm():
    estado_actual = estado_inactivo()
    next(estado_actual)  # Inicializa el primer estado

    while True:
        try:
            entrada = input("Ingresa una tecla (a–t) o 'exit': ").lower()
            if entrada == "exit":
                print("Ejecución de la FSM finalizada.")
                break

            estado_actual.send(entrada)

        except StopIteration:
            print("Estado final alcanzado o transición inválida.")
            break


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_fsm()

#--------------------------------------------------[ In English ]--------------------------------------------------

# FINITE STATE MACHINE FOR THE ROBOT TEST2

# Each state is implemented as a generator.
# Transitions occur based on received input characters.


def state_idle():
    print("Q1: Robot is idle")
    while True:
        event = yield
        if event == 'a':
            yield from state_move_to_table()
        else:
            break


def state_move_to_table():
    print("Q2: Moving towards the table")
    while True:
        event = yield
        if event == 'b':
            yield from state_move_to_table()
        elif event == 'c':
            yield from state_observe_table()
        elif event == 'd':
            yield from state_pick_object()
        elif event == 'e':
            yield from state_drop_object()
        else:
            break


def state_observe_table():
    print("Q3: Observing the table")
    while True:
        event = yield
        if event == 'f':
            yield from state_classify_object()
        elif event == 'g':
            yield from state_observe_table()
        else:
            break


def state_classify_object():
    print("Q4: Classifying the detected object")
    while True:
        event = yield
        if event == 't':
            yield from state_obstacle_alert()
        elif event == 'h':
            yield from state_move_to_table()
        else:
            break


def state_pick_object():
    print("Q5: Picking up the object")
    while True:
        event = yield
        if event == 'i':
            yield from state_navigate_destination()
        else:
            break


def state_navigate_destination():
    print("Q6: Navigating to destination")
    while True:
        event = yield
        if event == 'j':
            yield from state_move_to_table()
        elif event == 's':
            yield from state_obstacle_alert()
        else:
            break


def state_drop_object():
    print("Q7: Dropping the object")
    while True:
        event = yield
        if event == 'm':
            yield from state_verify_table()
        elif event == 'l':
            yield from state_drop_object()
        else:
            break


def state_verify_table():
    print("Q8: Verifying remaining objects on the table")
    while True:
        event = yield
        if event == 'n':
            yield from state_verify_table()
        elif event == 'o':
            yield from state_task_complete()
        else:
            break


def state_task_complete():
    print("Q9: Task completed successfully")
    while True:
        event = yield
        if event == 'p':
            yield from state_detect_obstacle()
        else:
            break


def state_detect_obstacle():
    print("Q10: Detecting obstacle")
    while True:
        event = yield
        if event == 'q':
            yield from state_move_to_table()
        else:
            break


def state_obstacle_alert():
    print("Q11: Obstacle detected – waiting for resolution")
    while True:
        event = yield
        if event == 'r':
            yield from state_move_to_table()
        else:
            break

# FSM EXECUTION CONTROLLER
def run_fsm():
    current_state = state_idle()
    next(current_state)  # Initialize first state

    while True:
        try:
            user_input = input("Enter a key (a–t) or 'exit': ").lower()
            if user_input == "exit":
                print("FSM execution stopped.")
                break

            current_state.send(user_input)

        except StopIteration:
            print("End state reached or invalid transition.")
            break


# Program entry point
if __name__ == "__main__":
    run_fsm()
