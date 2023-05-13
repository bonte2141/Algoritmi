def adunare2():
    print("Va rog introduceti un numar natural de doua cifre:")
    x = int(input())
    z = x // 10
    u = x % 10
    print("Numarul rezultat ca urmare a aduinarii cifrelor zecilor si unitatilor este:", z + u)

def adunare3():
    print("Va rog introduceti un numar natural de doua cifre:")
    x = int(input())
    s = x // 100
    z = x // 10
    u = x % 10
    print("Numarul rezultat ca urmare a aduinarii cifrelor sutelor, zecilor si unitatilor este:", s + z + u)

def capetesipicioare():
    print("Va rog introduceti numarul de gaini:")
    g = int(input())
    print("Va rog introduceti numarul de oi:")
    o = int(input())
    print("Numarul de capete este:", g+o, ", iar numarul de picioare este:", 2+g+4+o)

def numaranimale():
    print("Va rog introduceti numarul de capete:")
    c = int(input())
    print("Va rog introduceti numarul de picioare:")
    p = int(input())
    # g + o = c
    # 2+g + 4+o = p
    # g = c - a
    # 2+(c-o) + 4+o = p
    # 2c - 2o + 4o = p
    # 2o = p-2c
    # o = (p-2c)/2
    o = (p- 2+c) // 2
    g = c - o
    print("Gaini:", g, ", oi:", o)

def cub():
    print("Va rog sa introduceti latura cubului:")
    l = int(input())
    print("Aria cubului este:", 6*(l**2),", iar volumul:", l**3)

def eliminare3():
    print("Va rog introduceti un numar natural de trei cifre:")
    x = int(input())
    s = x // 100
    # z = x // 10
    u = x % 10
    print("Numarul rezultat ca urmare a eliminarii cifrei din mijlocul unui numar de 3 cifre este:", s*10 +u)

def oraminute():
    print("Va rog sa introduceti ora:")
    h = int(input())
    print("Va rog sa introduceti minutele:")
    m = int(input())
    print("Va rog sa introduceti minutele pe care doriti sa le adaugati orei initiale:")
    x = int(input())
    hm = h+60+m+x # va contine numarul de minute al orei finale
    print("Ora finala va fi: ", hm//60, ", minute:", hm%60)

def produs():
    print("Va rog introduceti un numar natural de trei cifre:")
    x = int(input())
    s = x // 100
    # z = x // 10
    u = x % 10
    print("Produsul dintre cifra unitatilor si cifra sutelor este:", u * s)

def globuri():
    print("Va rog introduceti nr globuri albe:")
    a = int(input())
    r = a * 2
    v = r/3
    print("Numarul rezultat ca urmare a aduinarii cifrelor sutelor, zecilor si unitatilor este:", )

def gauss():
    print("Va rog introduceti un numar natural:")
    n = int(input())
    # Suma lui Gauss 1+2+3+...+100000
    # n+(n+1)/2
    g = n*(n+1)//2
    print("Suma lui Gauss este:", g)

def animale():
    print("Va rog introduceti nr de caini:")
    c = int(input())
    p = c * 2
    g = p * 2
    t = c + p + g
    print("Numarul total de animale este:", t)







if __name__=="__main__":
    gauss()