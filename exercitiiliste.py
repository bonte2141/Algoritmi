# sa se determine minimul si maximul dintr-o lista
def min_max(lista):
    min = lista[0]
    max = lista[0]
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
        if lista[i] < min:
            min = lista[i]
    print(min, max)

    min1 = lista[0]
    max1 = lista[0]
    for i in range(len(lista)):
        if lista[i] > max1:
            max1 = lista[i]
        if lista[i] < min1:
            min1 = lista[i]
    print(min, min1, max, max1)

def metoda2(lista):
    lista.sort()
    min1 = lista[0]
    min2 = lista[1]
    max1 = lista(len(lista)-2)
    max2 = lista(len(lista)-1)
    print(min1, min2, max1, max2)

metoda2([2, 3, 45, 20, 1, 303, 34, 33])

def parcurgere_m(matrice):
    sir = "abcd" # sir de aceeasi dimensiune cu n
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            if matrice[i][j] == 1:
            print(sir[i], sir[j], end="/")

# sa se scrie o functie python recursiva care sa returneze numarul de cifre egale cu zero ale unui numar natural

def nr_zero(n):
    c = 0
    if n == 0:
        return 0
    if n % 10 == 0:
        c = 1
    return c + nr_zero(n // 10)








if __name__== '__main__':
    parcurgere_m([0,1,1],[1,0,1],[0,1,0],[1,1,1])