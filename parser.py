# Nueva línea para leer un número entero
c = int(input())
# Leer las dimensiones y datos de entrada
n, m, k = map(int, input().split())  # Lee tres números separados por espacios
nt = input().split()  # Lee una lista de no terminales (strings)
rules = [input() for _ in range(m)]  # Lee 'm' reglas de producción (strings)
strings = [input() for _ in range(k)]  # Lee 'k' cadenas a analizar (strings)

def obtener_letras_minusculas(rules):
    # Inicializar un conjunto para almacenar letras minúsculas únicas
    letras_minusculas = set()

    # Iterar sobre cada regla en el arreglo
    for regla in rules:
        # Obtener todas las letras minúsculas diferentes de 'e' de la regla
        letras = [char for char in regla if char.islower() and char != 'e']

        # Agregar las letras al conjunto
        letras_minusculas.update(letras)

    # Convertir el conjunto a una lista y retornarla
    return list(letras_minusculas)

E = obtener_letras_minusculas(rules)
grammar_symbol = E + V
inicial_symbol = "S"
inicial_symbol = "S"

def immediate_rec(S):
    recursives = []
    for i in V:
        x = i[0]
        parts = parts_of(i)
        for j in parts:
            if j[0] == x:
                recursives.append(j[0])

    aprobadas = []
    y = {}
    b = {}
    for i in recursives:
        b_values = []
        y_values = []
        parts = parts_of(i)
        cont = 0
        for j in parts:
            y_type = j[0]
            try:
                b_type = j[1]
            except:
                b_type =""
                pass
            if b_type in V or b_type in E:
                b_values.append(b_type)
                cont = cont + 1
            if y_type in V or y_type in E:
                if y_type != i:
                    y_values.append(y_type)
                    cont = cont + 1
            if cont == 2:
                aprobadas.append(i)
        y[i] = [y_values],[b_values]

    aprobadas_prima = []
    for i in range(len(aprobadas)):
        a = aprobadas[i]
        A_prima = a+"'"
        aprobadas_prima.append(A_prima)


def insertChar(mystring, position, chartoinsert ):
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring  

def parts_of(N):
    parts = []
    for i in range(0, len(rules)):
        if rules[i][0] == N:
            parts.append((rules[i].split("-"))[1])
    return parts

def parts_of_closure(N, R):
    parts = []
    for i in range(0, len(R)):
        if R[i][0] == N:
            parts.append((R[i].split("-"))[1])
    return parts

def check_leftrecursion(S):
    parts = parts_of(S)
    for x in parts:
        if x[0] in V:
            if x[0] == S:
                recursive = True
                return recursive
            else:
                a = check_leftrecursion(x)
                if a:
                    return a
    return False

def calculate_first(S):
    first = []
    parts = parts_of(S)

    if S in E:
        return S
    for i in range(0, len(parts)):
        for j in range(0, len(parts[i])):
            x = parts[i][j]
            if x in E:
                first.append(x)
                break
            if x in V:
                f = calculate_first(x)
                if "e" in f:
                    for elemento in f:
                        if elemento != "e":
                            first.append(elemento)
                else:
                    first.append(f)
                    break
            if "e" in parts:
                first.append("e")

    return first    

def calculate_follow(A):
    follow = []
    count = 0

    if A == inicial_symbol:
        follow.append("$")        
    for i in range(0, len(V)):
        parts = parts_of(V[i])
        for j in range(0, len(parts)):
            for k in range(0, len(parts[j])):
                count = k
                if parts[j][k] == A:
                    while True:
                        count = count + 1
                        if count - 1 != len(parts[j]) - 1:
                            f = calculate_first(parts[j][count])
                            for l in f:
                                if l != "e":
                                    follow.append(l)
                            if "e" in f:
                                continue
                            else:
                                break
                        else:
                            if count - 1 != len(parts[j]) - 1:
                                f = calculate_first(parts[j][count])
                                for l in f:
                                    if l != "e":
                                        follow.append(l)
                            if V[i] != A:
                                follow = follow + calculate_follow(V[i])

                            break
    
    return follow


def parsing_table():
    table = {}
    for i in range(len(rules)):
        first_A = calculate_first(rules[i][0])
        follow_A = calculate_follow(rules[i][0])
        if "e" in first_A and "$" not in follow_A:
            for b in range(len(follow_A)):
                table[(rules[i][0], follow_A[b])] = rules[i]
        elif "e" in first_A and "$" in follow_A:
            table[(rules[i][0], "$")] = rules[i]
        else:
            for a in range(len(first_A)):
                table[(rules[i][0], first_A[a])] = rules[i]
    return table

def predictive_parsing(string):
    str_index = 0
    T = ["$"]
    w = string
    a = w[str_index]
    X = T[-1]

    while X != "$":
        if X == a:
            T.pop()
            str_index += 1
            a = w[str_index] if str_index < len(w) else None 
        elif X in E:
            return "parsing failed"
        elif (X, a) not in parsingTable:
            return "parsing failed"
        else:
            production = parsingTable[(X, a)]
            T.pop()
            for p in reversed(parts_of(production[0])):
                T.append(p)
        X = T[-1]  
    if X == "$" and X == a:
        return "parsing successful"
    else:
        return "parsing failed"

def closure(I):
    global V
    J = I

    flag = False
    for i in range(0, len(J)):
        parts = parts_of_closure(J[i][0], J)
        for j in range(0, len(parts)):
            for k in range(0, len(grammar_symbol)):
                goto = go_to([J[i]], grammar_symbol[k])
                if len(goto) != 0 and goto not in J:
                    flag = True
                    J.append(goto)
    if flag == True:
        closure(J)
        
    return J

def go_to(I, X):
    goto = []
    for i in range(0, len(I)):
        parts = parts_of_closure(I[i][0], I)
        
        for j in range(0, len(parts)):
            if X in parts[j]:
                if len(parts[j]) > 1 and parts[j][parts[j].index(X) - 1] == ".":
                    a  = parts[j].replace(".", "")
                    a = insertChar(a, parts[j].index(X), ".")
                    if (I[i][0] + "-" + a) not in goto:
                        goto.append(I[i][0] + "-" + a)
    value_return = closure(goto)
    return (value_return)

def set_of_items(G):
    flag = False    

    for i in range(0, len(C)):
        for j in range(0, len(C[i])):
            for k in range(0, len(grammar_symbol)):
                goto = go_to([C[i][j]], grammar_symbol[k])
                if len(goto) != 0 and goto not in C:
                    flag = True
                    C.append(goto)
    if flag == True:
        set_of_items(G)

    return C