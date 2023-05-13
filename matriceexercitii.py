# se da o matrice patratica, sa se calculeze o matrice patratica si sa se determine elementul care contine valoarea minima si maxima

def matrice_patratica(matrice):
    m = len(matrice)
    n = len(matrice(0))
    min = 99999
    max = 0
    imax = ""
    imin = ""
    for i in range(m):
        for j in range(n):
            if matrice[i][j]> max:
                max = matrice[i][j]
                imax = i + "," + j
            if matrice[i][j]< min:
                min = matrice[i][j]
                imax = i + "," + j
    print("Matrice", max)
    print("Matrice", min)

# se da o matrice patratica, sa se genereze elementele matricii dupa urmatoarele reguli:
# elementele pentru care produsul indicilor este un numar par vor avea valoarea 1
# elementele pentru care produsul indicilor este un numar impar vor avea valoarea 0
# elementele de pe diagolana prioncipala vor avea valoarea 2

def matrice(matrice):
    m = len(matrice)
    n = len(matrice[0])
    for i in range(m):
        for j in range(n):
            if ij % 2 == 0:
                matrice[i][j] = 1
            if ij % 2 != 0:
                matrice[i][j] = 0
            if i==j:
                matrice[i][j] = 2


def unire(listas, listad):
    rezultat = []
    i = 0
    j = 0
    while i<len(listas) and j<len(listad):
        if(listas[i]<listad[j]):
            rezultat.append(listas[i])
            i = i+1
        else:
            rezultat.append(listad[j])
            j = j+1
    while i<len(listas):
        rezultat.append(listas[i])
        i = i+1
    while i<len(listad):
        rezultat.append(listad[j])
        j = j+1
    return rezultat

def msort(lista):
    if len(lista)<=1:
        return lista
    else:
        mij = len(lista)//2
        stanga = msort(lista[:mij])
        dreapta = msort(lista[mij:])

        return unire(stanga, dreapta)