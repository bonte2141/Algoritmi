graph = [[0, 1], [0, 2],
         [1, 2], [1, 3],
         [2, 4], [2, 6],
         [4, 5],
         [5, 7]]

parcurs = []
lp = []

def parcurgeregraph(graph, start):
    if start not in lp:
        parcurs.append(start)
        for element in graph:
            if element[0] == start and start not in lp:
                lp.append(start)
                parcurgeregraph(graph, element[1])

parcurgeregraph(graph, 4)
print(parcurs)


cale = []

def parcurgereit(graph, start):
    currentnode = start
    cale.append(currentnode)
    for element in graph:
        if element[0] == currentnode:
            currentnode = element[1]
            cale.append(currentnode)
    return(cale)

def toatecaile(graph):
    cai = []
    n = len(graph)
    i = 0
    while i<n:
        primelement = graph[0][0]
        cai.append(parcurgereit(graph, primelement))
        graph.pop(0)
        i = i + 1
    print(cai)