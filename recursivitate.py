def cautaresir(sirprincipal, subsir):
    i = 0
    n = len(sirprincipal) - len(subsir)
    while i<= n:
        j = 0
        while j<len(subsir):
            if sirprincipal[i+j]!=subsir[j]:
                j = j + 1
                break
            else:
                j = j + 1
            if j == len(subsir):
                return i
        i = i + j
    return -1


def adunare(n): # 1 + 2 + 3 + 4 + 5 ...
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


def adunarerec(n):
    if n==1:
        return 1
    return n + adunarerec(n-1)


def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)


def fib(n): # al n-lea termen din sirul lui Fibonacci
    f = 0
    t1 = 0
    t2 = 1
    for i in range(2,n+1):
        f = t1 + t2
        t1 = t2
        t2 = f
    return f

# Fibonacci recursiv
# F(n) = F(n-1)+F(n-2)
def fibrec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibrec(n-1)+ fibrec(n-2)

# De realizat o functie recursiva care isi determina numarul de aparitii al cifrei 0 intr-un numar natural
def nr_zero_sir(n): # n este un numar natural
    sir = str(n) # convertesc numarul natural la sir
    c = 0
    if sir[len(sir)-1]=="0":
        c = 1
    if len(sir)-1<=0:
        return c
    return c + nr_zero_sir(int(sir[:len(sir)-1]))

def nr_zero(n):
    c = 0
    if n==0:
        return 0
    if n%10==0:
        c = 1
    return c + nr_zero(n//10)

# Sa se realizeze o functie care ia ca parametru un numar natural
# si il reintoarce in ordine inversa a elementelor numarului.
# 210001 - 1 0 0 0 1 2

def inversare(n):
    sir = str(n)  # convertesc nr,natural in sir
    c = sir[len(sir)-1]  # extrag ultimul element
    if len(sir)-1 <= 0:  # verific daca nu cumva am ajuns la sfarsit
        return c
    return c + " , " + inversare(int(sir[:len(sir) - 1]))





if __name__ == "__main__":
    print(inversare(2100111010))