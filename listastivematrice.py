def lista():
    l = [108, 1081, 340, 200, 500, 10, 40, 120]
    print(l)
    # suma elementelor din a doua jumatate a listei
    suma = 0
    for i in range(len(l)):
        if i >= len(l) // 2:
            suma += l[i]
    print("Suma elementelor din jumatatea superioara este:", suma)
    # suma elementelor mai mari decat 200
    suma = 0
    for element in l:
        if element > 200:
            element += suma
    print("Suma elementelor mai mari decat 200 este:", suma)
    for i in range(len(l)):
        print("l[",i,"]=", l[i], end=",")
        l.append(156)
        l.append(45)
        l.append(900)
        # l.insert(0, 100000)
        for i in range(len(l)):
            print("l[",i,"]=" ,l[i], end=",")
        l.pop()
        print("")
        print(l)
        l.pop()
        print(l)
        l.insert(0, 100000)
        print(l)
        l.pop(0)
        print(l)



def exemplu_deque():
    from  collections import deque
    l2 = deque()
    l1 = list()
    l1.append(100)
    l2.append(100)
    l1.append(1000)
    l2.append(1000)
    l1.append(150)
    l2.append(150)
    l1.append(300)
    l2.append(300)
    l1.append(10)
    l2.append(10)
    print(l1)
    print(l2)
    l2.pop()
    print(l2)

def matrice():
    matrice=[] # fiecare element al listei mele este la randul sau o lista
    nr_randuri = 3
    nr_coloane = 3
    matrice = [[0] * nr_coloane] * nr_randuri
    print(matrice)
    for i in range(nr_randuri):
        # coloane_matrice=[]
        for j in range(nr_coloane):
            print("(", i,",", j,")=", end="")
            matrice [i][j] = int(input())
    print(matrice)

    suma = 0
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            if i == j:
                suma += matrice[i][j]
    print(suma)
    lista_suma_coloane = [0] * nr_coloane
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            lista_suma_coloane[j] += matrice [i][j]
    print(lista_suma_coloane)


if __name__ == "__main__":
    exemplu_deque()