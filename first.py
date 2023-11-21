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

"""
rules = ["S-AaAb", "S-BbBa", "A-e", "B-e"]
E = ["a", "b"]
V = ["S", "A", "B"]
"""
rules = ["S-(S)", "S-e"]
E = ["(", ")"]
V = ["S"]



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

FIRST = calculate_first("S")
print(FIRST)



def calculate_follow(A):
    follow = []
    if A == "S":
        follow.append("$")
    for i in range(len(V)):
        parts = parts_of(V[i])
        for j in range(len(parts)):
            for k in range(len(parts[j])):
                x = parts[j][k]
                if x == A:
                    if k == (len(parts[j])-1):
                        follow.append(calculate_follow(V[i]))
                    if k <= (len(parts[j])-2):
                        next = parts[j][k+1]
                        print(f"se le va a calcular el first_next a {next}")
                        if next in V:
                            first_next = calculate_first(next)
                        if next in E:
                            first_next = next
                        print(f"el first del next es => {first_next}")
                        if "e" in first_next:
                            print(f"epaleee")
                            for elemento in first_next:
                                if elemento != "e":
                                    follow.append(elemento)
                        else:
                            print(f"epalongooo")
                            follow.append(first_next)
                #break
    return follow                
                    
    

FOLLOW = calculate_follow("S")
print(FOLLOW)



    