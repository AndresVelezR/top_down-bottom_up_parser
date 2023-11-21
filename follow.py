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
                    print(count)
                    while True:
                        count = count + 1
                        print(count)
                        print(len(parts[j]) - 1)
                        if count - 1 != len(parts[j]) - 1:
                            f = calculate_first(parts[j][count])
                            for l in f:
                                if l != "e":
                                    print(l)
                                    follow.append(l)
                            print("e" in f)
                            if "e" in f:
                                continue
                            else:
                                break
                        else:
                            print("---")
                            print(k)
                            print(len(parts[j]) - 1)
                            print(count)
                            print("---")
                            if count - 1 != len(parts[j]) - 1:
                                f = calculate_first(parts[j][count])
                                for l in f:
                                    if l != "e":
                                        print(l)
                                        follow.append(l)
                            if V[i] != A:
                                follow = follow + calculate_follow(V[i])

                            break
    
    return follow
