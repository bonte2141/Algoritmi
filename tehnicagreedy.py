def greedy():
    lista_timpi_reparatie_masini = [2, 3, 50, 20, 10, 3, 2, 5, 1]
    lista_masini_reparate = []
    T = int(input("Timp maxim de lucru: "))
    lista_timpi_reparatie_masini.sort()
    t_ramas = T
    i = 0
    for i in range(len(lista_timpi_reparatie_masini)):
        if lista_timpi_reparatie_masini[i] <= t_ramas:
            t_ramas = t_ramas - lista_timpi_reparatie_masini[i]
            lista_masini_reparate.append(lista_timpi_reparatie_masini[i])

    print(lista_masini_reparate)
    print(t_ramas)

def suma_recursiv(lista):
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return lista[0]
        else:
            return 0
    else:
        mijloc = len(lista) // 2
        return suma_recursiv(lista[:mijloc]) + suma_recursiv(lista[mijloc:])








if __name__ == "__main__":