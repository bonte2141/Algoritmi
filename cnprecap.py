#Definiti o functie care face cautarea intr-o lista, iar daca elementul este gasit, imi reintoarce o pozitie, altfel -1

def cautare(list, element):
    for i in range (len(list)):
        if list[i] == element:
            return i
    return -1
print(cautare([1, 2, 40, 50, 20, 0], 20))

def generareCNP(gen, an, luna, zi, judet, nnn):
    CNP = ""
    if gen == "M" or gen == "m" or gen == "masculin":
        if an < 2000:
            CNP += "1"
        else:
            CNP += "5"
    else:
            if an < 2000:
                CNP += "2"
            else:
                CNP += "6"
    if an < 2000:
            an = an - 1900
    else:
            an = an - 2000
    if an < 10:
            CNP += "0"
    CNP += str(an)
    if luna<10:
            CNP += "0"
    CNP += str(luna)
    if zi<10:
            CNP += "0"
    CNP += str(zi)
    if judet<10:
            CNP += "0"
    CNP += str(judet)
    if nnn<10:
            CNP += "00"
    elif nnn<100:
            CNP += "0"
    else:
            CNP += ""
    CNP += str(nnn)
    CNP += str(generareC(CNP))
    return CNP

def generareC(sir):
    sirControl = "279146358279"
    suma = 0
    for i in range(len(sir)):
        suma += int(sir[i])*int(sirControl[i])
    if suma%11 == 10:
        return 1
    else:
        return suma % 11
print(generareCNP("m", 1980, 1, 1, 24, 999))