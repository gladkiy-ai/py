from pprint import pprint
""" ****** Стандартный алгоритм обхода графа в глубину. ****
1. Начните с размещения любой вершины графа на вершине стека.
2. Возьмите верхний элемент стека и добавьте его в список посещенных.
3. Создайте список смежных узлов этой вершины. Добавьте те, 
 которых нет в списке посещенных, в начало стека.
4. Продолжайте повторять шаги 2 и 3, пока стек не станет пустым.
"""
def dfs(graph, start, visited=[]):
    if start not in visited:
        visited.append(start)
        for neighbour in graph[start]:
            if neighbour in graph.keys():
                dfs(graph, neighbour, visited)

def dfs_max_deep(graph, start, visited=[]):
    d = 1
    if start not in visited:
        visited.append(start)
        for neighbor in graph[start]:
            if neighbour in graph.keys():
                d = max(d, dfs_max_deep(graph, neighbor, visited) + 1)
    return d

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
    a16 = ('A16', 16)
    a17 = ('A17', 17)
    a18 = ('A18', 18)
    a98 = ('A98', 98)
    a99 = ('A99', 99)
    b10 = ('B10', 10)
    b11 = ('B11', 11)
    b12 = ('B12', 12)
    b13 = ('B13', 13)
    b25 = ('B25', 25)
    b26 = ('B26', 26)
    b27 = ('B27', 27)
    b28 = ('B28', 28)
    b29 = ('B29', 29)
    b30 = ('B30', 30)

    graph1 = {a01: a02,
             a02: a03,
             a03: a04,
             a04: a05,
             a05: a16,
             a16: a17,
             a17: a18,
             a18: a98,
             a98: a99
              }
    graph2 = {b10: b11,
             b11: b12,
             b12: b13,
             b13: b25,
             b25: b26,
             b26: b27,
             b27: b28,
             b28: b29,
             b29: b30
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
    # print(dfs(graph2,b10))
    # print(dfs_max_deep(graph2,b10))
    # graph3 = concatGraph(graph1, graph2)
    # pprint(graph3)
    # isOrder(graph3)
