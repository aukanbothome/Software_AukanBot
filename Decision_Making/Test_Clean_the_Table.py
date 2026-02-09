#--------------------------------------------------[En Español]--------------------------------------------------

# Máquina de estados para el reto 5: Restaurant
def q1():
    print("Q1: Mantenerse quieto (remaining_idle)")
    while True:
        char = yield
        if char == 'a':
            yield from q2()
        else:
            break

def q2():
    print("Q2: Observar clientes en la fila (watching_queue)")
    while True:
        char = yield
        if char == 'b':
            yield from q2()
        elif char == 'c':
            yield from q3()
        else:
            break

def q3():
    print("Q3: Navegar hacia la mesa del cliente (going_to_customer_table)")
    while True:
        char = yield
        if char == 'd':
            yield from q2()
        elif char == 'e':
            yield from q4()
        else:
            break

def q4():
    print("Q4: Tomar pedido (taking_order)")
    while True:
        char = yield
        if char == 'f':
            yield from q2()
        elif char == 'g':
            yield from q5()
        else:
            break

def q5():
    print("Q5: Confirmar pedido (confirming_order)")
    while True:
        char = yield
        if char == 'h':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Ir a la cocina (returning_to_kitchen)")
    while True:
        char = yield
        if char == 'i':
            yield from q7()
        else:
            break

def q7():
    print("Q7: Recoger el pedido (picking_up_order)")
    while True:
        char = yield
        if char == 'j':
            yield from q8()
        else:
            break

def q8():
    print("Q8: Llevar pedido al cliente (delivering_order)")
    while True:
        char = yield
        if char == 'k':
            yield from q9()
        elif char == 'p':
            yield from q10()
        else:
            break

def q9():
    print("Q9: Finalizar turno (ending_shift)")
    while True:
        char = yield
        if char == 'n':
            yield from q2()
        else:
            break

def q10():
    print("Q10: Solicitar instrucciones humanas (requesting_instructions)")
    while True:
        char = yield
        if char == 'o':
            yield from q10()
        elif char == 'q':
            yield from q8()
        else:
            break

def q11():
    print("Q11: Gestionar obstáculos (handling_obstacle)")
    while True:
        char = yield
        if char == 'r':
            yield from q11()
        elif char == 's':
            yield from q10()
        elif char == 't':
            yield from q2()
        else:
            break

# Controlador principal de la máquina de estados
def fsm():
    state = q1()
    next(state)
    while True:
        try:
            char = input("Presiona una tecla (a–t) o 'exit' para salir: ").lower()
            if char == 'exit':
                break
            state.send(char)
        except StopIteration:

#--------------------------------------------------[ In English ]--------------------------------------------------

# State machine for Challenge 5: Restaurant

def q1():
    print("Q1: Remaining idle")
    while True:
        char = yield
        if char == 'a':
            yield from q2()
        else:
            break

def q2():
    print("Q2: Watching customers in the queue")
    while True:
        char = yield
        if char == 'b':
            yield from q2()
        elif char == 'c':
            yield from q3()
        else:
            break

def q3():
    print("Q3: Navigating to the customer's table")
    while True:
        char = yield
        if char == 'd':
            yield from q2()
        elif char == 'e':
            yield from q4()
        else:
            break

def q4():
    print("Q4: Taking the order")
    while True:
        char = yield
        if char == 'f':
            yield from q2()
        elif char == 'g':
            yield from q5()
        else:
            break

def q5():
    print("Q5: Confirming the order")
    while True:
        char = yield
        if char == 'h':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Going back to the kitchen")
    while True:
        char = yield
        if char == 'i':
            yield from q7()
        else:
            break

def q7():
    print("Q7: Picking up the order")
    while True:
        char = yield
        if char == 'j':
            yield from q8()
        else:
            break

def q8():
    print("Q8: Delivering the order to the customer")
    while True:
        char = yield
        if char == 'k':
            yield from q9()
        elif char == 'p':
            yield from q10()
        else:
            break

def q9():
    print("Q9: Ending shift")
    while True:
        char = yield
        if char == 'n':
            yield from q2()
        else:
            break

def q10():
    print("Q10: Requesting human instructions")
    while True:
        char = yield
        if char == 'o':
            yield from q10()
        elif char == 'q':
            yield from q8()
        else:
            break

def q11():
    print("Q11: Handling obstacles")
    while True:
        char = yield
        if char == 'r':
            yield from q11()
        elif char == 's':
            yield from q10()
        elif char == 't':
            yield from q2()
        else:
            break

# Main FSM controller
def fsm():
    state = q1()
    next(state)
    while True:
        try:
            char = input("Press a key (a–t) or 'exit' to quit: ").lower()
            if char == 'exit':
