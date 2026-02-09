# --------------------------------------------------[ En Español ]--------------------------------------------------

# MÁQUINA DE ESTADOS – MANEJO DE OBJETOS
# El robot puede almacenar objetos o
# servir cereal, reaccionando a obstáculos.


def estado_inactivo():
    print("Q1: Robot en reposo")
    while True:
        evento = yield
        if evento == 'a':
            yield from estado_ir_mesa()
        elif evento == 'n':
            yield from estado_servir_cereal()
        else:
            break


def estado_ir_mesa():
    print("Q2: Navegando hacia la mesa")
    while True:
        evento = yield
        if evento == 'b':
            yield from estado_seleccionar_objeto()
        elif evento == 'c':
            yield from estado_ir_mesa()
        elif evento == 'k':
            yield from estado_obstaculo()
        else:
            break


def estado_seleccionar_objeto():
    print("Q3: Seleccionando objeto")
    while True:
        evento = yield
        if evento == 'd':
            yield from estado_seleccionar_objeto()
        elif evento == 'e':
            yield from estado_transportar_objeto()
        else:
            break


def estado_transportar_objeto():
    print("Q4: Transportando objeto al almacenamiento")
    while True:
        evento = yield
        if evento == 'f':
            yield from estado_transportar_objeto()
        elif evento == 'g':
            yield from estado_guardar_objeto()
        elif evento == 'n':
            yield from estado_obstaculo()
        else:
            break


def estado_guardar_objeto():
    print("Q5: Guardando objeto")
    while True:
        evento = yield
        if evento == 'o':
            yield from estado_finalizar_tarea()
        else:
            break


def estado_servir_cereal():
    print("Q6: Sirviendo cereal")
    while True:
        evento = yield
        if evento == 'j':
            yield from estado_finalizar_tarea()
        else:
            break


def estado_finalizar_tarea():
    print("Q7: Tarea finalizada")
    while True:
        evento = yield
        if evento == 'i':
            yield from estado_inactivo()
        else:
            break


def estado_obstaculo():
    print("Q8: Obstáculo detectado")
    while True:
        evento = yield
        if evento == 'l':
            yield from estado_ir_mesa()
        elif evento == 'm':
            yield from estado_transportar_objeto()
        else:
            break


def ejecutar_fsm():
    estado_actual = estado_inactivo()
    next(estado_actual)

    while True:
        try:
            entrada = input("Ingresa una tecla (a–o) o 'exit': ").lower()
            if entrada == "exit":
                print("FSM detenida.")
                break

            estado_actual.send(entrada)

        except StopIteration:
            print("Estado final o transición inválida.")
            break


if __name__ == "__main__":
    ejecutar_fsm()

# FSM SECUENCIAL – TAREA DE ALMACENAMIENTO
# Implementación usando variable de estado
# y estructura match-case.


estado = "IR_A_ZONA_PRUEBA"

posicion_inicio = "punto_inicial"
posicion_gabinete = "frente_al_gabinete"
posicion_mesa = "mesa_objetos"
posicion_juez = "ubicacion_juez"

objetos_detectados = []
almacen = {}

while estado != "FIN":

    match estado:

        case "IR_A_ZONA_PRUEBA":
            print("Moviéndose al área de prueba...")
            estado = "DETECTAR_OBJETOS"

        case "DETECTAR_OBJETOS":
            print("Detectando objetos sobre la mesa...")
            objetos_detectados = ["manzana", "naranja", "plátano", "caja_cereal"]
            estado = "CLASIFICAR_OBJETOS"

        case "CLASIFICAR_OBJETOS":
            print("Clasificando objetos por categoría...")
            almacen = {
                "frutas": ["manzana", "naranja", "plátano"],
                "cereales": ["caja_cereal"]
            }
            estado = "ABRIR_GABINETE"

        case "ABRIR_GABINETE":
            print("Abriendo la puerta del gabinete...")
            estado = "GUARDAR_OBJETOS"

        case "GUARDAR_OBJETOS":
            for categoria, lista in almacen.items():
                for obj in lista:
                    print(f"Guardando {obj} en el estante de {categoria}.")
            estado = "REGRESAR_INICIO"

        case "REGRESAR_INICIO":
            print(f"Regresando al punto inicial: {posicion_inicio}")
            estado = "REPORTAR"

        case "REPORTAR":
            print(f"Informando al juez en {posicion_juez}")
            print("La tarea fue completada exitosamente.")
            estado = "FIN"

print("Secuencia finalizada. Robot listo para una nueva tarea.")

# --------------------------------------------------[ In English ]--------------------------------------------------

# FINITE STATE MACHINE – OBJECT HANDLING
# This FSM controls a robot that either
# stores objects or pours cereal, handling
# obstacles when necessary.


def state_idle():
    print("Q1: Robot is idle")
    while True:
        event = yield
        if event == 'a':
            yield from state_go_to_table()
        elif event == 'n':
            yield from state_pour_cereal()
        else:
            break


def state_go_to_table():
    print("Q2: Navigating to the table")
    while True:
        event = yield
        if event == 'b':
            yield from state_select_object()
        elif event == 'c':
            yield from state_go_to_table()
        elif event == 'k':
            yield from state_obstacle()
        else:
            break


def state_select_object():
    print("Q3: Selecting an object")
    while True:
        event = yield
        if event == 'd':
            yield from state_select_object()
        elif event == 'e':
            yield from state_transport_object()
        else:
            break


def state_transport_object():
    print("Q4: Transporting object to storage")
    while True:
        event = yield
        if event == 'f':
            yield from state_transport_object()
        elif event == 'g':
            yield from state_store_object()
        elif event == 'n':
            yield from state_obstacle()
        else:
            break


def state_store_object():
    print("Q5: Storing object")
    while True:
        event = yield
        if event == 'o':
            yield from state_finish_task()
        else:
            break


def state_pour_cereal():
    print("Q6: Pouring cereal")
    while True:
        event = yield
        if event == 'j':
            yield from state_finish_task()
        else:
            break


def state_finish_task():
    print("Q7: Task completed")
    while True:
        event = yield
        if event == 'i':
            yield from state_idle()
        else:
            break


def state_obstacle():
    print("Q8: Obstacle detected")
    while True:
        event = yield
        if event == 'l':
            yield from state_go_to_table()
        elif event == 'm':
            yield from state_transport_object()
        else:
            break

# FSM CONTROLLER
def run_fsm():
    current_state = state_idle()
    next(current_state)

    while True:
        try:
            user_input = input("Enter a key (a–o) or 'exit': ").lower()
            if user_input == "exit":
                print("FSM stopped.")
                break

            current_state.send(user_input)

        except StopIteration:
            print("End state reached or invalid transition.")
            break


if __name__ == "__main__":
    run_fsm()

# SEQUENTIAL FSM – STORAGE TASK
# This version uses a state variable and
# match-case instead of generators.


state = "MOVE_TO_TEST_AREA"

start_position = "starting_point"
cabinet_position = "cabinet_front"
table_position = "object_table"
judge_position = "judge_location"

detected_objects = []
storage = {}

while state != "END":

    match state:

        case "MOVE_TO_TEST_AREA":
            print("Moving to the test area...")
            state = "DETECT_OBJECTS"

        case "DETECT_OBJECTS":
            print("Detecting objects on the table...")
            detected_objects = ["apple", "orange", "banana", "cereal_box"]
            state = "CLASSIFY_OBJECTS"

        case "CLASSIFY_OBJECTS":
            print("Classifying objects by category...")
            storage = {
                "fruits": ["apple", "orange", "banana"],
                "cereals": ["cereal_box"]
            }
            state = "OPEN_CABINET"

        case "OPEN_CABINET":
            print("Opening cabinet door...")
            state = "STORE_OBJECTS"

        case "STORE_OBJECTS":
            for category, items in storage.items():
                for item in items:
                    print(f"Placing {item} in the {category} shelf.")
            state = "RETURN_HOME"

        case "RETURN_HOME":
            print(f"Returning to starting position: {start_position}")
            state = "REPORT"

        case "REPORT":
            print(f"Reporting task completion to judge at {judge_position}")
            print("All objects stored successfully.")
            state = "END"

print("Sequence finished. Robot ready for a new task.")
