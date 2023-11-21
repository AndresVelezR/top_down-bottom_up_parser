#rules = ["S-aSb", "A-a", "A-c", "A-e", "A-b"]
"""
rules = ["S-Bb", "S-Cd", "B-aB", "B-e", "C-cC", "C-e"]
E = ["a", "b", "c", "d"]
V = ["S", "A", "B", "C"]

"""
"""
rules = ["S-A", "A-Bb", "A-Cd", "B-aB", "B-e", "C-cC", "C-e"]
E = ["a", "b", "c", "d"]
V = ["S", "A", "B", "C"]
"""
rules = ["S-AaAb", "S-BbBa", "A-e", "B-e"]
E = ["a", "b"]
V = ["S", "A", "B"]


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
"""
FIRST = calculate_first("B")
print(FIRST)
"""


def calculate_follow(A):
    follow = []
    if A == "S":
        follow.append("$")
        print(f"A es => {A}")
        print(f"Se añade $ al follow")
        print(f"el follow va asi => {follow}")
    for i in range(len(V)):
        parts = parts_of(V[i])
        print(f"se escogen las partes de los no terminales")
        print(f"parts va asi => {parts}")
        for j in range(len(parts)):
            for k in range(len(parts[j])):
                x = parts[j][k]
                if x == A:
                    print(f"x es => {x}")
                    if k <= (len(parts[j])-2):
                        
                        next = parts[j][k+1]
                        
                        first_next = calculate_first(next)
                        print(f"x = {x} no esta en la ultima posicion de la produ")
                        print(f"el simbolo siguiente a {x} es {next}")
                        print(f"el fist de next es => {first_next}")
                        if "e" in first_next:
                            print(f"e esta en el first del next")
                            for elemento in first_next:
                                if elemento != "e":
                                    follow.append(elemento)
                                    print(f"se añade el elemento {elemento} del next al follow")
                                    print(f"el follow va asi => {follow}")
                        else:
                            follow.append(first_next)
                            print(f"no hay e en el first del next")
                            print(f"se eñade el first_next al follow")
                            print(f"el follow va asi => {follow}")
                    if k == (len(parts[j])-1):
                        follow.append(calculate_follow(V[i]))
                        print(f"x = {x} esta en la ultima posicion")
                        print(f"se añade el follow del no terminal que deriva en la produccion")
                        print(f"el follow va asi => {follow}")
    return follow

FOLLOW = calculate_follow("A")
print(FOLLOW)

