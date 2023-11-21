#rules = ["S-aSb", "A-a", "A-c", "A-e", "A-b"]

# rules = ["S-Bb", "S-Cd", "B-aB", "B-e", "C-cC", "C-e"]
# E = ["a", "b", "c", "d"]
# V = ["S", "A", "B", "C"]

# rules = ["S-A", "A-Bb", "A-Cd", "B-aB", "B-e", "C-cC", "C-e"]
# E = ["a", "b", "c", "d"]
# V = ["S", "A", "B", "C"]

# rules = ["S-AaAb", "S-BbBa", "A-e", "B-e"]
# E = ["a", "b"]
# V = ["S", "A", "B"]

# rules = ["S-ABCDE", "A-a", "A-e", "B-b", "B-e", "C-c", "D-d", "D-e", "E-x", "E-e"]
# E = ["d", "c", "b", "a", "x"]
# V = ["A", "B", "C", "D", "E", "S"]

# rules = ["P-xQRS", "Q-yz", "Q-z", "R-w", "R-e", "S-y"]
# E = ["x", "y", "z", "w"]
# V = ["P", "Q", "R"," S"]

rules = ["S-aBDh", "B-cC", "C-bC", "C-e", "D-EF", "E-g", "E-e", "F-f", "F-e"]
E = ["a", "h", "c", "b", "g", "f"]
V = ["S", "B", "C", "D", "E", "F"]


inicial_symbol = "S"

#Lado derecho de una produccion
def parts_of(N):
    parts = []
    for i in range(0, len(rules)):
        if rules[i][0] == N:
            parts.append((rules[i].split("-"))[1])
    return parts

def calculate_first(S):
    first = []
    parts = parts_of(S)
    print(f"SE ESCOGEN LAS PARTES DE {S} => {parts}")

    if S in E:
        return S
    for i in range(0, len(parts)):
        for j in range(0, len(parts[i])):
            x = parts[i][j]
            print(f"x es => {x}")
            if x in E:
                print(f"{x} pertenece a los terminales")
                first.append(x)
                print(f"se añade {x} al first")
                print(f"EL FIRST VA ASI => {first}")
                break
            if x in V:
                print(f"{x} pertenece a los  NO-terminales")
                f = calculate_first(x)
                print(f"Se calcula el first de {x} y es => {f}")
                if "e" in f:
                    print(f"e esta en f")
                    for elemento in f:
                        if elemento != "e":
                            first.append(elemento)
                            print(f"se añade el f al first sin epsilon")
                            print(f"el first queda asi => {first}")
                else:
                    first.append(f)
                    print(f"no habia e en f, se añade f a first")
                    print(f" el fisrt va asi => {first}")
                    break
            if "e" in parts:
                first.append("e")
                print(f"e esta en partes de {S}, se añade al first")
                print(f"el first va asi => {first}")
    return first    

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