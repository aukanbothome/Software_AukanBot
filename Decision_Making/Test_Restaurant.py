#--------------------------------------------------[ En Español ]--------------------------------------------------

def q1():
    print("Q1: Permanecer inactivo")
    while True:
        char = yield
        if char == 'a':
            yield from q2()
        else:
            break

def q2():
    print("Q2: Observando la fila")
    while True:
        char = yield
        if char == 'b':
            yield from q2()
        elif char == 'c':
            yield from q3()
        else:
            break

def q3():
    print("Q3: Dirigiéndose a la mesa del cliente")
    while True:
        char = yield
        if char == 'd':
            yield from q3()
        elif char == 'e':
            yield from q4()
        elif char == 'f':
            yield from q11()
        else:
            break

def q4():
    print("Q4: Tomando el pedido")
    while True:
        char = yield
        if char == 'g':
            yield from q5()
        else:
            break

def q5():
    print("Q5: Confirmando el pedido")
    while True:
        char = yield
        if char == 'h':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Regresando a la cocina")
    while True:
        char = yield
        if char == 'i':
            yield from q7()
        elif char == 'z':
            yield from q11()
        else:
            break

def q7():
    print("Q7: Recogiendo el pedido")
    while True:
        char = yield
        if char == 'k':
            yield from q8()
        else:
            break

def q8():
    print("Q8: Entregando el pedido")
    while True:
        char = yield
        if char == 'l':
            yield from q9()
        elif char == 'm':
            yield from q10()
        else:
            break

def q9():
    print("Q9: Finalizando turno")
    while True:
        char = yield
        if char == 'n':
            yield from q2()
        else:
            break

def q10():
    print("Q10: Solicitando instrucciones humanas")
    while True:
        char = yield
        if char == 'o':
            yield from q2()
        elif char == 'p':
            yield from q10()
        else:
            break

def q11():
    print("Q11: Gestionando obstáculo")
    while True:
        char = yield
        if char == 'r':
            yield from q6()
        elif char == 's':
            yield from q8()
        elif char == 'q':
            yield from q3()
        else:
            break

#--------------------------------------------------[ In English ]--------------------------------------------------

def q1():
    print("Q1: Remaining idle")
    while True:
        char = yield
        if char == 'a':
            yield from q2()
        else:
            break

def q2():
    print("Q2: Watching queue")
    while True:
        char = yield
        if char == 'b':
            yield from q2()
        elif char == 'c':
            yield from q3()
        else:
            break

def q3():
    print("Q3: Going to customer table")
    while True:
        char = yield
        if char == 'd':
            yield from q3()
        elif char == 'e':
            yield from q4()
        elif char == 'f':
            yield from q11()
        else:
            break

def q4():
    print("Q4: Taking order")
    while True:
        char = yield
        if char == 'g':
            yield from q5()
        else:
            break

def q5():
    print("Q5: Confirming order")
    while True:
        char = yield
        if char == 'h':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Returning to kitchen")
    while True:
        char = yield
        if char == 'i':
            yield from q7()
        elif char == 'z':
            yield from q11()
        else:
            break

def q7():
    print("Q7: Picking up order")
    while True:
        char = yield
        if char == 'k':
            yield from q8()
        else:
            break

def q8():
    print("Q8: Delivering order")
    while True:
        char = yield
        if char == 'l':
            yield from q9()
        elif char == 'm':
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
    print("Q10: Requesting instructions")
    while True:
        char = yield
        if char == 'o':
            yield from q2()
        elif char == 'p':
            yield from q10()
        else:
            break

def q11():
    print("Q11: Handling obstacle")
    while True:
        char = yield
        if char == 'r':
            yield from q6()
        elif char == 's':
            yield from q8()
        elif char == 'q':
            yield from q3()
        else:
            break
