from pprint import pprint

def concatGraph(graph_1, graph_2):
    graph_out ={}
    #добавить поочереди key из первого графа1
    #проверять есть ли такой key в value,
    #если да то добавить цепочку из графа2
    return graph_1

def isOrder(graph):
    for node in graph.keys():
        if isOrderUtils(graph, node) == False:
            return print("Graph is not ordered")
    return print("Graph is ordered")

def isOrderUtils(graph, v):
    order = False

    for neighbour in graph[v]:
        if neighbour in graph.keys():
            if neighbour[1] > v[1]:
                order = True
            if order == True:
                if isOrderUtils(graph, neighbour) == True:
                    return True
            else:
                return False
        else:
            if graph[v][1] > v[1]:
                return True
            else:
                return False
    return False


def isCyclicUtil(graph, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbour in graph[v]:
            if neighbour in graph.keys():
                if visited[neighbour] == False:
                    if isCyclicUtil(graph,neighbour, visited, recStack) == True:
                        return True
                elif recStack[neighbour] == True:
                    return True

        recStack[neighbour] = False
        return False

def isCyclic(graph):
        visited = dict.fromkeys(graph.keys(), False)
        recStack = dict.fromkeys(graph.keys(), False)
        for node in graph.keys():
            if visited[node] == False:
                if isCyclicUtil(graph, node, visited, recStack) == True:
                    return print("Graph has a cycle")
        return print("Graph has no cycle")

if __name__ == '__main__':
    a01 = ('A01', 1)
    a02 = ('A02', 2)
    a03 = ('A03', 3)
    a04 = ('A04', 4)
    a05 = ('A05', 5)
    a06 = ('A06', 16)
    a07 = ('A07', 17)
    a08 = ('A08', 18)
    a09 = ('A09', 98)
    a10 = ('A10', 99)
    b01 = ('B01', 10)
    b02 = ('B02', 11)
    b03 = ('B03', 12)
    b04 = ('B04', 13)
    b05 = ('B05', 25)
    b06 = ('B06', 26)
    b07 = ('B07', 27)
    b08 = ('B08', 28)
    b09 = ('B09', 29)
    b10 = ('B10', 30)

    graph1 = {a01: a02,
             a02: a03,
             a03: a04,
             a04: a05,
             a05: a06,
             a06: a07,
             a07: a08,
             a08: a09,
             a09: a10
              }

    graph2 = {b01: b02,
             b02: b03,
             b04: [a07, b10],
             a07: [b05, b07],
             b05: b06,
             b06: b07,
             b07: b08,
             b08: b09,
             b09: b10
              }
    print('graph1--------------------------')
    pprint(graph1)
    print('graph2--------------------------')
    pprint(graph2)
    print('isCyclic grahp2---------------------------')
    isCyclic(graph2)
    print('isOrder graph2---------------------------')
    isOrder(graph2)
    # print('Concat graph1 + graph 2---------------------------')
    # graph3 = concatGraph(graph1, graph2)
    # pprint(graph3)
    # isOrder(graph3)

