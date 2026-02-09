#--------------------------------------------------[ En Español ]--------------------------------------------------

def q1():
    print("Q1: Permanecer en reposo")
    while True:
        char = yield
        if char == 'a':
            yield from q2()
        else:
            break

def q2():
    print("Q2: Dirigiéndose a la mesa")
    while True:
        char = yield
        if char == 'b':
            yield from q2()
        elif char == 'c':
            yield from q3()
        elif char == 'd':
            yield from q5()
        elif char == 'e':
            yield from q7()
        else:
            break

def q3():
    print("Q3: Observando la mesa")
    while True:
        char = yield
        if char == 'f':
            yield from q4()
        elif char == 'g':
            yield from q3()
        else:
            break

def q4():
    print("Q4: Clasificando objeto")
    while True:
        char = yield
        if char == 't':
            yield from q11()
        elif char == 'h':
            yield from q2()
        else:
            break

def q5():
    print("Q5: Tomando objeto")
    while True:
        char = yield
        if char == 'i':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Navegando hacia el destino")
    while True:
        char = yield
        if char == 'j':
            yield from q2()
        elif char == 's':
            yield from q11()
        else:
            break

def q7():
    print("Q7: Soltando objeto")
    while True:
        char = yield
        if char == 'm':
            yield from q8()
        if char == 'l':
            yield from q7()
        else:
            break

def q8():
    print("Q8: Verificando objetos en la mesa")
    while True:
        char = yield
        if char == 'n':
            yield from q8()
        elif char == 'o':
            yield from q9()
        else:
            break

def q9():
    print("Q9: Completando la tarea")
    while True:
        char = yield
        if char == 'p':
            yield from q10()
        else:
            break

def q10():
    print("Q10: Detectando obstáculo")
    while True:
        char = yield
        if char == 'q':
            yield from q2()
        else:
            break

def q11():
    print("Q11: Obstáculo detectado")
    while True:
        char = yield
        if char == 'r':
            yield from q2()
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
    print("Q2: Going to table")
    while True:
        char = yield
        if char == 'b':
            yield from q2()
        elif char == 'c':
            yield from q3()
        elif char == 'd':
            yield from q5()
        elif char == 'e':
            yield from q7()
        else:
            break

def q3():
    print("Q3: Looking at table")
    while True:
        char = yield
        if char == 'f':
            yield from q4()
        elif char == 'g':
            yield from q3()
        else:
            break

def q4():
    print("Q4: Classifying object")
    while True:
        char = yield
        if char == 't':
            yield from q11()
        elif char == 'h':
            yield from q2()
        else:
            break

def q5():
    print("Q5: Picking object")
    while True:
        char = yield
        if char == 'i':
            yield from q6()
        else:
            break

def q6():
    print("Q6: Navigating to destination")
    while True:
        char = yield
        if char == 'j':
            yield from q2()
        elif char == 's':
            yield from q11()
        else:
            break

def q7():
    print("Q7: Dropping object")
    while True:
        char = yield
        if char == 'm':
            yield from q8()
        if char == 'l':
            yield from q7()
        else:
            break

def q8():
    print("Q8: Verifying table items")
    while True:
        char = yield
        if char == 'n':
            yield from q8()
        elif char == 'o':
            yield from q9()
        else:
            break

def q9():
    print("Q9: Completing task")
    while True:
        char = yield
        if char == 'p':
            yield from q10()
        else:
            break

def q10():
    print("Q10: Detecting obstacle")
    while True:
        char = yield
        if char == 'q':
            yield from q2()
        else:
            break

def q11():
    print("Q11: Obstacle detected")
    while True:
        char = yield
        if char == 'r':
            yield from q2()
        else:
            break
