def matrice1():
    n = 4
    sdp = 0
    sds = 0
    matrice = [[0] * n for  in range(n)]

    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i<j: # elementul este deasupra diagonalei principale
                sdp += matrice[i][j]
            if i+j<n-1: # elementul este deasuipra diagonalei secundare
                sds += matrice[i][j]
    print("SDP=", sdp)
    print("SDS,", sds)

def matrice2():
    m = 5
    n = 4
    matrice = [[0] * n for  in range(n)]

    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j]*2
    print(matrice)

def matrice3():
    m = 5
    n = 4
    matrice = [[0] n for  in range(n)]

    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j]+10
    print(matrice)

def lista():
    l = input().split(",")
    contor = 0
    for index in range(len(l)):
        if l[index] == "100":
            contor = index

    print(contor)

def matrice4():
    n = int(input("n="))
    m = int(input("m="))
    s=0
    matrice = [[0]*n for  in range(m)]
    for i in range(m):
        for j in range(n):
            if matrice[i][j]%2==0:
                s+=matrice[i][j]






if name == "main":
    matrice4()