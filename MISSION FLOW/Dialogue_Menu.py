#--------------------------------------------------[ En Español ]--------------------------------------------------

def Help_me_carry():
    """
    Prueba: Help Me Carry
    El robot asiste al operador siguiéndolo,
    recogiendo un objeto y regresando al punto inicial.
    """

    print("[Node_pose_estimation] Explorando el entorno para localizar al operador")
    print("[Node_pose_estimation] Operador identificado, asignando ID")
    print("[Node_TTS] Estoy listo para seguirte")

    print("[Node_path_planning] Siguiendo al operador a una distancia segura")

    print("[Node_path_planning] Ajustando ruta para evitar obstáculos")
    print("[Node_path_planning] Supervisando el entorno con sensores")

    print("[Node_object_detection] Buscando el carrito y el bolso")
    print("[Node_armcontrol] Tomando el bolso del carrito")

    print("[Node_path_planning] Regresando a la posición inicial")
    print("[Node_path_planning] Recalculando trayectoria para evitar colisiones")
    print("[Node_armcontrol] Dejando el bolso en el suelo")

    print("[Node_pose_estimation] Verificando si existe una fila")
    print("[Node_path_planning] Ubicándose al final de la fila")

    print("[LOG] ✅ Prueba completada: Help Me Carry")


def General_Purpose_Service_Robot():
    """
    Prueba: General Purpose Service Robot
    El robot interpreta comandos en lenguaje natural
    y ejecuta tareas de servicio.
    """

    print("[Node_TTS] Hola, estoy listo para ayudarte. Indícame tu solicitud.")

    user_commands = [
        "Give Pepito in the kitchen the knife that is in the living room",
        "I'm cold",
        "Take a pen to Juan"
    ]

    for command in user_commands:
        print(f"[Node_STT] Comando recibido: {command}")

        if "knife" in command:
            obj, origin, destination = "knife", "living room", "kitchen"
        elif "cold" in command:
            obj, origin, destination = "blanket", "closet", "user"
        elif "pen" in command:
            obj, origin, destination = "pen", "desk", "Juan"
        else:
            print("[Node_LLM] No se pudo interpretar el comando")
            continue

        print(f"[Node_LLM] Intención detectada → Objeto: {obj}, Origen: {origin}, Destino: {destination}")
        print(f"[Node_path_planning] Navegando hacia {origin}")
        print(f"[Node_object_detection] Localizando {obj}")
        print(f"[Node_armcontrol] Sujetando {obj}")
        print(f"[Node_path_planning] Transportando {obj} a {destination}")
        print(f"[Node_armcontrol] Entregando {obj}")

    print("[LOG] ✅ Prueba completada: General Purpose Service Robot")


def Receptionist():
    """
    Prueba: Receptionist
    El robot recibe invitados, recopila información
    y los presenta entre sí.
    """

    guests = []
    interests = []

    for i in range(2):
        print("[Node_object_detection] Invitado detectado en la entrada")
        print("[Node_armcontrol] Abriendo la puerta")
        print("[Node_TTS] ¡Bienvenido! ¿Cuál es tu nombre?")
        name = f"Invitado_{i+1}"
        print(f"[Node_STT] Nombre detectado: {name}")

        print("[Node_TTS] Por favor acompáñame a la mesa de bebidas")
        print("[Node_path_planning] Guiando al invitado")
        print("[Node_Head] Orientando la cabeza en la dirección de navegación")

        print("[Node_TTS] Mientras caminamos, dime algo que te guste")
        interest = "música"
        print(f"[Node_STT] Interés detectado: {interest}")

        print("[Node_TTS] ¿Cuál es tu bebida favorita?")
        drink = "jugo"
        print(f"[Node_STT] Bebida seleccionada: {drink}")
        print("[Node_object_detection] Verificando disponibilidad")
        print(f"[Node_TTS] Puedes tomar el {drink}")

        print("[Node_TTS] ¿Deseas ir al living?")
        print("[Node_path_planning] Acompañando al invitado al living")
        print("[Node_Head] Ajustando orientación")

        print("[Node_TTS] Este es tu asiento, por favor siéntate")

        guests.append({"name": name, "drink": drink, "interest": interest})
        interests.append(interest)

    print("[Node_TTS] Permítanme presentarlos")
    print(f"[Node_TTS] Ambos comparten interés en {guests[0]['interest']}")

    print("[Node_Head] Observando la interacción")
    print("[LOG] Prueba completada: Receptionist")


def Storing_Groceries():
    """
    Prueba: Storing Groceries
    El robot clasifica y almacena objetos
    según su categoría.
    """

    objects = ["apple", "orange", "cereal_box", "bottle", "banana"]

    print("[Node_path_planning] Navegando hacia la mesa de objetos")
    print("[Node_object_detection] Detectando y clasificando productos")

    for obj in objects:
        print(f"[Node_Reasoning] Clasificando {obj}")

    print("[Node_armcontrol] Abriendo gabinetes")
    print("[Node_armcontrol] Guardando objetos en los estantes correspondientes")
    print("[Node_armcontrol] Vertiendo cereal en su contenedor")

    print("[Node_path_planning] Regresando al punto inicial")
    print("[Node_TTS] Todos los objetos han sido almacenados correctamente")
    print("✅ [LOG] Prueba completada: Storing Groceries")


def Clean_the_Table():
    """
    Prueba: Clean the Table
    El robot despeja la mesa y utiliza el lavavajillas.
    """

    print("[Node_path_planning] Dirigiéndose a la mesa")
    print("[Node_object_detection] Identificando objetos")

    print("[Node_armcontrol] Abriendo el lavavajillas")
    print("[Node_armcontrol] Manipulando utensilios")

    print("[Node_armcontrol] Colocando detergente")
    print("[Node_armcontrol] Limpiando el área de bebidas")

    print("[Node_path_planning] Regresando a la posición inicial")
    print("[Node_TTS] Limpieza completada")
    print("✅ [LOG] Prueba completada: Clean the Table")


def Enhanced_General_Purpose_Service_Robot():
    """
    Prueba: Enhanced GPSR
    El robot detecta problemas en el entorno
    y actúa de forma autónoma.
    """

    issues = [
        "Lámpara encendida sin personas",
        "Basura en el suelo",
        "Refrigerador abierto"
    ]

    for issue in issues:
        print(f"[Node_LLM] Problema detectado: {issue}")
        print("[Node_Reasoning] Planificando solución")
        print("[Node_path_planning] Desplazándose al área afectada")
        print("[Node_armcontrol] Ejecutando acción correctiva")
        print("[Node_TTS] Problema solucionado")

    print("[LOG] ✅ Prueba completada: Enhanced GPSR")


def Restaurant():
    """
    Prueba: Restaurant
    El robot toma un pedido, lo recoge
    y lo entrega al cliente.
    """

    print("[Node_pose_estimation] Detectando interacción del cliente")
    print("[Node_TTS] Hola, ¿desea ordenar algo?")

    print("[Node_path_planning] Aproximándose a la mesa")
    print("[Node_TTS] ¿Qué desea ordenar?")
    print("[Node_STT] Pedido recibido: jugo de naranja")

    print("[Node_path_planning] Dirigiéndose al bar")
    print("[Node_armcontrol] Recogiendo la bebida con bandeja")

    print("[Node_path_planning] Regresando a la mesa")
    print("[Node_armcontrol] Sirviendo el pedido")
    print("[Node_TTS] Disfrute su bebida")

    print("✅ [LOG] Prueba completada: Restaurant")


def Give_Me_a_Hand():
    """
    Prueba: Give Me a Hand
    El robot recibe objetos del operador
    y los coloca en el lugar indicado.
    """

    print("[Node_path_planning] Ingresando al área de prueba")
    print("[Node_pose_estimation] Operador detectado")

    items = ["control remoto", "libro", "vaso"]

    for item in items:
        print(f"[Usuario] Por favor toma el {item}")
        print("[Node_armcontrol] Aproximándose a la mano del operador")
        print("[Node_armcontrol] Recibiendo objeto")
        print("[Node_path_planning] Navegando al destino")
        print("[Node_armcontrol] Colocando objeto")

    print("[Node_TTS] ¿Necesitas algo más?")
    print("✅ [LOG] Prueba completada: Give Me a Hand")

#--------------------------------------------------[ In English ]--------------------------------------------------

def Help_me_carry():
    """
    Task: Help Me Carry
    The robot assists the operator by following them,
    picking up an object, and returning to the starting area.
    """

    # --- Operator following ---
    print("[Node_pose_estimation] Scanning environment to locate the operator...")
    print("[Node_pose_estimation] Operator detected, assigning tracking ID")
    print("[Node_TTS] I am ready to follow you")

    print("[Node_path_planning] Maintaining a safe following distance")

    # --- Obstacle avoidance ---
    print("[Node_path_planning] Updating trajectory to avoid obstacles")
    print("[Node_path_planning] Monitoring surroundings using sensors")

    # --- Object pickup ---
    print("[Node_object_detection] Searching for the cart and the bag")
    print("[Node_armcontrol] Grasping the bag from the cart")

    # --- Return phase ---
    print("[Node_path_planning] Navigating back to the initial position")
    print("[Node_path_planning] Replanning path to prevent collisions")
    print("[Node_armcontrol] Releasing the bag on the ground")

    # --- Optional: join the line ---
    print("[Node_pose_estimation] Checking if a queue is present")
    print("[Node_path_planning] Positioning at the end of the line")

    print("[LOG] ✅ Task successfully completed: Help Me Carry")


def General_Purpose_Service_Robot():
    """
    Task: General Purpose Service Robot
    The robot interprets natural language commands
    and executes service-oriented actions.
    """

    print("[Node_TTS] Hello, I am ready to assist you. Please tell me your request.")

    user_commands = [
        "Give Pepito in the kitchen the knife that is in the living room",
        "I'm cold",
        "Take a pen to Juan"
    ]

    for command in user_commands:
        print(f"[Node_STT] User command received: {command}")

        # Simulated semantic understanding
        if "knife" in command:
            obj, origin, destination = "knife", "living room", "kitchen"
        elif "cold" in command:
            obj, origin, destination = "blanket", "closet", "user"
        elif "pen" in command:
            obj, origin, destination = "pen", "desk", "Juan"
        else:
            print("[Node_LLM] Command could not be interpreted")
            continue

        print(f"[Node_LLM] Parsed intent → Object: {obj}, Source: {origin}, Target: {destination}")
        print(f"[Node_path_planning] Navigating to {origin}")
        print(f"[Node_object_detection] Locating object: {obj}")
        print(f"[Node_armcontrol] Picking up {obj}")
        print(f"[Node_path_planning] Transporting {obj} to {destination}")
        print(f"[Node_armcontrol] Delivering {obj}")

    print("[LOG] ✅ Task completed: General Purpose Service Robot")


def Receptionist():
    """
    Task: Receptionist
    The robot welcomes guests, gathers information,
    and introduces them to each other.
    """

    guests = []
    interests = []

    for i in range(2):
        print("[Node_object_detection] Guest detected at the entrance")
        print("[Node_armcontrol] Opening the door")
        print("[Node_TTS] Welcome! May I know your name?")
        name = f"Guest_{i+1}"
        print(f"[Node_STT] Name detected: {name}")

        print("[Node_TTS] Please follow me to the drink table")
        print("[Node_path_planning] Guiding guest to the drink table")
        print("[Node_Head] Orienting head towards navigation direction")

        print("[Node_TTS] While we walk, tell me something you like")
        interest = "music"
        print(f"[Node_STT] Interest detected: {interest}")

        print("[Node_TTS] What is your preferred drink?")
        drink = "juice"
        print(f"[Node_STT] Drink selected: {drink}")
        print("[Node_object_detection] Verifying drink availability")
        print(f"[Node_TTS] You may take the {drink}")

        print("[Node_TTS] Shall I guide you to the living room?")
        print("[Node_path_planning] Escorting guest to the living room")
        print("[Node_Head] Adjusting gaze direction")

        print("[Node_TTS] This is your seat, please have a seat")

        guests.append({"name": name, "drink": drink, "interest": interest})
        interests.append(interest)

    print("[Node_TTS] Let me introduce you both")
    print(f"[Node_TTS] {guests[0]['name']} meet {guests[1]['name']}")
    print(f"[Node_TTS] You both like {guests[0]['interest']}")

    print("[Node_Head] Observing interaction between guests")
    print("[LOG] Task completed: Receptionist")


def Storing_Groceries():
    """
    Task: Storing Groceries
    The robot classifies objects and stores them
    according to category and shelf level.
    """

    objects = ["apple", "orange", "cereal_box", "bottle", "banana"]

    print("[Node_path_planning] Navigating to the table with objects")
    print("[Node_object_detection] Detecting and classifying items")

    for obj in objects:
        print(f"[Node_Reasoning] Assigning category to {obj}")

    print("[Node_armcontrol] Opening cabinet doors")

    print("[Node_armcontrol] Picking and placing objects in the cabinet")
    print("[Node_armcontrol] Pouring cereal into container")

    print("[Node_path_planning] Returning to the starting position")
    print("[Node_TTS] All groceries have been stored correctly")
    print("✅ [LOG] Task completed: Storing Groceries")


def Clean_the_Table():
    """
    Task: Clean the Table
    The robot clears the table and loads items into the dishwasher.
    """

    objects = ["fork", "knife", "plate", "glass1", "glass2"]

    print("[Node_path_planning] Moving to the table")
    print("[Node_object_detection] Identifying objects on the table")

    print("[Node_armcontrol] Opening dishwasher and pulling tray")

    for obj in objects:
        print(f"[Node_armcontrol] Handling object: {obj}")
        print("[Node_armcontrol] Placing object in the appropriate location")

    print("[Node_armcontrol] Adding detergent tablet")
    print("[Node_armcontrol] Cleaning the drink area")

    print("[Node_path_planning] Returning to home position")
    print("[Node_TTS] Table cleaning task completed")
    print("✅ [LOG] Task finished: Clean the Table")


def Enhanced_General_Purpose_Service_Robot():
    """
    Task: Enhanced GPSR
    The robot detects problems and autonomously solves them.
    """

    issues = [
        "Lamp turned on in empty room",
        "Trash detected on the floor",
        "Refrigerator door left open"
    ]

    for issue in issues:
        print(f"[Node_LLM] Detected issue: {issue}")
        print("[Node_Reasoning] Planning corrective action")
        print("[Node_path_planning] Moving to issue location")
        print("[Node_armcontrol] Executing solution")
        print("[Node_TTS] Problem resolved")

    print("[LOG] ✅ Task completed: Enhanced GPSR")


def Restaurant():
    """
    Task: Restaurant
    The robot takes an order, collects it from the bar,
    and delivers it to the client.
    """

    print("[Node_pose_estimation] Detecting client interaction")
    print("[Node_TTS] Hello, may I take your order?")

    print("[Node_path_planning] Navigating to the table")
    print("[Node_TTS] What would you like to order?")
    print("[Node_STT] Order received: orange juice")

    print("[Node_path_planning] Going to the bar")
    print("[Node_armcontrol] Picking up the drink using a tray")

    print("[Node_path_planning] Returning to the table")
    print("[Node_armcontrol] Serving the order")
    print("[Node_TTS] Enjoy your drink")

    print("✅ [LOG] Task completed: Restaurant")


def Give_Me_a_Hand():
    """
    Task: Give Me a Hand
    The robot receives objects from the operator
    and places them at the requested location.
    """

    print("[Node_path_planning] Entering the test area")
    print("[Node_pose_estimation] Operator detected")

    items = ["remote control", "book", "glass"]

    for item in items:
        print(f"[User] Please take the {item}")
        print("[Node_armcontrol] Approaching operator's hand")
        print("[Node_armcontrol] Receiving object")
        print("[Node_path_planning] Navigating to destination")
        print("[Node_armcontrol] Placing object")

    print("[Node_TTS] Do you need anything else?")
    print("✅ [LOG] Task completed: Give Me a Hand")
