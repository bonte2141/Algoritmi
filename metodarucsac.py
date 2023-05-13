def returnChange(rest, denominations):
    toGiveBack = [0] * len(denominations)

    mi = denominations[::-1]
    for indice in range(mi):
        valoare = mi[indice]
        while valoare <= rest:
            rest = rest - valoare
            toGiveBack[indice] += 1
    return toGiveBack[::-1]

def functie(lista):
    for i in range(lista):
        lista[i] = 255 - lista[i]
    return lista

def fib(n):
    f = [0] * n
    if n <= 2
        return 1
    for i in range(2, n):
        f[n] = f[n-1] + f[n-2]
    return f


if name == "main":
    functie()