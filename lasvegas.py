#Din lista de adiacenta [[0,1][0,2][1,2][1,3][3,4]] sa se construiasca matricea prezentata.
def nr(lista):
    maxim = 0
    for elemente in lista:
        for e in elemente:
            if e > maxim:
                maxim = e
    return maxim
matrice = [ ]
n = nr(lista)
    for i in range(n):
        rand = [ ]
    for j in range(n):
        rand.append(0)
    matrice.append(rand)
    for element in lista:
        x = element(0)
        y = element(1)
    matrice[x],[y] = 1
    matrice[y],[x] = 1

def lista_adiacenta(mat):
    lista = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]==1 and i > j:
                lista.append([i,j])

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == dice2:
        return true
    else:
        return false
    for i in range(1000)
        v r = roll.dice()