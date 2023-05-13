def schimbare():
    cuvint = input()
    print (cuvint)
    cuvintn = ""
    index = 0
    for caracter in cuvint:
        print(caracter, "<->", cuvint[index])
        if caracter in "aeiou":
            cuvintn = cuvintn + caracter.upper()
        else:
            cuvintn = cuvintn + caracter
        print(cuvintn)
        index = index + 1


def transformare():
    cuvint = input()
    print (cuvint)
    cuvintn = ""
    index = 0
    for caracter in cuvint:
        print(caracter, "<->", cuvint[index])
        if index == 0 or index == len(cuvint)-1:
            cuvintn = cuvintn + caracter.upper()
        else:
            cuvintn = cuvintn + caracter
        print(cuvintn)
        index = index + 1

def adaugare_prefix_sufix():
    prefix = "#"
    sufix = "_"
    cuvint = input()
    cuvintn = prefix + cuvint +sufix
    print(cuvintn)



def extragere_prefix_sufix():
    nr_catactere_de_extras = 2
    cuvint = input()
    print(cuvint[::])


def asterix():
    cuvint = input()
    print (cuvint)
    cuvintn = ""
    index = 0
    for caracter in cuvint:
        print(caracter, "<->", cuvint[index])
        if caracter in "aeiou":
            cuvintn = cuvintn + caracter + "*"
        else:
            cuvintn = cuvintn + caracter
        print(cuvintn)
        index = index + 1


def eliminare():
    cuvint = input()
    print (cuvint)
    cuvintn = ""
    index = 0
    for caracter in cuvint:
        print(caracter, "<->", cuvint[index])
        if caracter in "aeiou":
            cuvintn = cuvintn
        else:
            cuvintn = cuvintn + caracter
        print(cuvintn)
        index = index + 1


def lista():
    l = [234, 345, 100, 90, 70, 50, 10, 3, 2, 7]
    print(l)
    jumatate = len(l) // 2
    l1 = l[:jumatate:]
    print(l1)
    l1.sort()
    l2 = l[jumatate::]
    print(l2)
    l2.sort(reverse=True)
    print(l2)


def countlista():
    l = [20, 10, 20, 10, 0, 0, 30, 45, 10]
    print(l)
    contor = l.count(20)
    print (contor)
    s = "aaabbbboooooaaaaahn"
    contor = s.count("a")
    print(contor)



if __name__== "__main__":