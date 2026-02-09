#--------------------------------------------------[ En Español ]--------------------------------------------------

def q1():
    print("Q1: Permanecer en reposo")
    while True:
        char = yield
        if char == 'a':
            yield from q1()
        else:
            break

def q2():
    print("Q2: Navegando hacia el operador")
    while True:
        char = yield
        if char == 'b':
            yield from q2()
        elif char == 'c':
            yield from q3()
        elif char == 'd':
            yield from q10()
        else:
            break

def q3():
    print("Q3: Recibiendo objeto")
    while True:
        char = yield
        if char == 'e':
            yield from q3()
        elif char == 'f':
            yield from q4()
        else:
            break

def q4():
    print("Q4: Interpretando comando")
    while True:
        char = yield
        if char == 'g':
            yield from q4()
        elif char == 'h':
            yield from q10()
        elif char == 'i':
            yield from q5()
        else:
            break

def q5():
    print("Q5: Solicitando confirmación")
    while True:
        char = yield
        if char == 'j':
            yield from q5()
        elif char == 'k':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Navegando hacia el objetivo")
    while True:
        char = yield
        if char == 'm':
            yield from q6()
        elif char == 'n':
            yield from q7()
        elif char == 'o':
            yield from q10()
        else:
            break

def q7():
    print("Q7: Colocando objeto")
    while True:
        char = yield
        if char == 'p':
            yield from q7()
        elif char == 'q':
            yield from q8()
        else:
            break

def q8():
    print("Q8: Regresando al operador")
    while True:
        char = yield
        if char == 'r':
            yield from q8()
        elif char == 's':
            yield from q9()
        else:
            break

def q9():
    print("Q9: Tarea completada")
    while True:
        char = yield
        if char == 'u':
            yield from q2()
        else:
            break

def q10():
    print("Q10: Gestionando obstáculo")
    while True:
        char = yield
        if char == 'x':
            yield from q10()
        elif char == 'v':
            yield from q6()
        else:
            break

#--------------------------------------------------[ In English ]--------------------------------------------------

def q1():
    print("Q1: Remaining idle")
    while True:
        char = yield
        if char == 'a':
            yield from q1()
        else:
            break

def q2():
    print("Q2: Navigating to operator")
    while True:
        char = yield
        if char == 'b':
            yield from q2()
        elif char == 'c':
            yield from q3()
        elif char == 'd':
            yield from q10()
        else:
            break

def q3():
    print("Q3: Receiving object")
    while True:
        char = yield
        if char == 'e':
            yield from q3()
        elif char == 'f':
            yield from q4()
        else:
            break

def q4():
    print("Q4: Interpreting command")
    while True:
        char = yield
        if char == 'g':
            yield from q4()
        elif char == 'h':
            yield from q10()
        elif char == 'i':
            yield from q5()
        else:
            break

def q5():
    print("Q5: Requesting confirmation")
    while True:
        char = yield
        if char == 'j':
            yield from q5()
        elif char == 'k':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Navigating to target")
    while True:
        char = yield
        if char == 'm':
            yield from q6()
        elif char == 'n':
            yield from q7()
        elif char == 'o':
            yield from q10()
        else:
            break

def q7():
    print("Q7: Placing object")
    while True:
        char = yield
        if char == 'p':
            yield from q7()
        elif char == 'q':
            yield from q8()
        else:
            break

def q8():
    print("Q8: Returning to operator")
    while True:
        char = yield
        if char == 'r':
            yield from q8()
        elif char == 's':
            yield from q9()
        else:
            break

def q9():
    print("Q9: Task completed")
    while True:
        char = yield
        if char == 'u':
            yield from q2()
        else:
            break

def q10():
    print("Q10: Handling obstacle")
    while True:
        char = yield
        if char == 'x':
            yield from q10()
        elif char == 'v':
            yield from q6()
        else:
            break
