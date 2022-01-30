#https://russianblogs.com/article/27221255944/
from pprint import pprint

def getGraphKeys(in_graph):
    for key in in_graph.keys():
            print(key)

def isOrder(graph):

    for node in graph.keys():
        print(f'first order = ' + str(node) )
        if isOrderUtils(graph, node) == False:
            return print("Graph is not ordered")
    return print("Graph is ordered")

def isOrderUtils(graph, v):
    # Отметить текущий узел как посещенный и добавляет в стек рекурсии
    order = False

    # Повтор для всех соседей если любой сосед посещен и в recStack, то график циклический
    print('v=' + str(v)+' graph[v] = '+str(graph[v])+' len(graph[v]) ='+str(len(graph[v])))

    # if graph[v] in graph.keys():
    #     print('graph[v] in graph.keys()')
    #     if graph[v][1] > v[1]:
    #         NOT_order = False

    for neighbour in graph[v]:
        print('before neighbour=' + str(neighbour)+' v=' + str(v))
        if neighbour in graph.keys():
            if neighbour[1] > v[1]:
                order = True
            print(f'neighbour = ' + str(neighbour) +' v = ' + str(v) +
                  ' neighbour[1] = ' + str(neighbour[1]) +' v[1] = ' + str(v[1]) +' NOT_order = ' + str(order))
            if order == True:
                if isOrderUtils(graph, neighbour) == True:
                    return True
            else:
                return False
        else:
            print(f'graph[v] = ' + str(graph[v]) + ' v = ' + str(v) +
                  ' graph[v][1] = ' + str(graph[v][1]) + ' v[1] = ' + str(v[1]) + ' NOT_order = ' + str(order))
            if graph[v][1] > v[1]:
                return True
            else:
                return False
    # Узел должен быть извлечен из стек рекурсии до завершения функции
    print('return NOT_order =' + str(order))
    return False



def isCyclicUtil(graph, v, visited, recStack):
        # Отметить текущий узел как посещенный и добавляет в стек рекурсии
        visited[v] = True
        recStack[v] = True

        # Повтор для всех соседей если любой сосед посещен и в recStack, то график циклический
        print('v='+str(v))
        for neighbour in graph[v]:
            if neighbour in graph.keys():
                print(f'neighbour = ' + str(neighbour) + ' visited[v] = ' + str(visited[neighbour]) + ' recStack[v] = '
                  + str(recStack[neighbour]))
                if visited[neighbour] == False:
                    if isCyclicUtil(graph,neighbour, visited, recStack) == True:
                        return True
                elif recStack[neighbour] == True:
                    return True

        # Узел должен быть извлечен из стек рекурсии до завершения функции
        recStack[neighbour] = False
        return False
    # Возвращает true, если график циклический, иначе false

def isCyclic(graph):
        visited = dict.fromkeys(graph.keys(), False)
        print(visited)
        recStack = dict.fromkeys(graph.keys(), False)
        print(recStack)
        for node in graph.keys():
            print(f'visited['+str(node)+']='+str(visited[node]))
            if visited[node] == False:
                if isCyclicUtil(graph, node, visited, recStack) == True:
                    return print("Graph has a cycle")
        return print("Graph has no cycle")

if __name__ == '__main__':
    a = ('A', 1)
    b = ('B', 2)
    c = ('C', 3)
    d = ('D', 4)
    e = ('E', 5)
    f = ('F', 6)

    graph = {a: b,
             b: c,
             c: d}
    print('graph--------------------------')
    pprint(graph)
    print('getGraphKeys---------------------------')
    pprint(getGraphKeys(graph))
    print('isCyclic---------------------------')
    isCyclic(graph)
    print('isOrderUtils---------------------------')
    print(isOrderUtils(graph, a))
    print('isOrder---------------------------')
    isOrder(graph)

def getGraphKeys(in_graph):
    for key in in_graph.keys():
            print(key)

def isOrder(graph):

    for node in graph.keys():
        print(f'first order = ' + str(node) )
        if isOrderUtils(graph, node) == False:
            return print("Graph is not ordered")
    return print("Graph is ordered")

def isOrderUtils(graph, v):
    # Отметить текущий узел как посещенный и добавляет в стек рекурсии
    order = False

    # Повтор для всех соседей если любой сосед посещен и в recStack, то график циклический
    print('v=' + str(v)+' graph[v] = '+str(graph[v])+' len(graph[v]) ='+str(len(graph[v])))

    # if graph[v] in graph.keys():
    #     print('graph[v] in graph.keys()')
    #     if graph[v][1] > v[1]:
    #         NOT_order = False

    for neighbour in graph[v]:
        print('before neighbour=' + str(neighbour)+' v=' + str(v))
        if neighbour in graph.keys():
            if neighbour[1] > v[1]:
                order = True
            print(f'neighbour = ' + str(neighbour) +' v = ' + str(v) +
                  ' neighbour[1] = ' + str(neighbour[1]) +' v[1] = ' + str(v[1]) +' NOT_order = ' + str(order))
            if order == True:
                if isOrderUtils(graph, neighbour) == True:
                    return True
            else:
                return False
        else:
            print(f'graph[v] = ' + str(graph[v]) + ' v = ' + str(v) +
                  ' graph[v][1] = ' + str(graph[v][1]) + ' v[1] = ' + str(v[1]) + ' NOT_order = ' + str(order))
            if graph[v][1] > v[1]:
                return True
            else:
                return False
    # Узел должен быть извлечен из стек рекурсии до завершения функции
    print('return NOT_order =' + str(order))
    return False



def isCyclicUtil(graph, v, visited, recStack):
        # Отметить текущий узел как посещенный и добавляет в стек рекурсии
        visited[v] = True
        recStack[v] = True

        # Повтор для всех соседей если любой сосед посещен и в recStack, то график циклический
        print('v='+str(v))
        for neighbour in graph[v]:
            if neighbour in graph.keys():
                print(f'neighbour = ' + str(neighbour) + ' visited[v] = ' + str(visited[neighbour]) + ' recStack[v] = '
                  + str(recStack[neighbour]))
                if visited[neighbour] == False:
                    if isCyclicUtil(graph,neighbour, visited, recStack) == True:
                        return True
                elif recStack[neighbour] == True:
                    return True

        # Узел должен быть извлечен из стек рекурсии до завершения функции
        recStack[neighbour] = False
        return False
    # Возвращает true, если график циклический, иначе false

def isCyclic(graph):
        visited = dict.fromkeys(graph.keys(), False)
        print(visited)
        recStack = dict.fromkeys(graph.keys(), False)
        print(recStack)
        for node in graph.keys():
            print(f'visited['+str(node)+']='+str(visited[node]))
            if visited[node] == False:
                if isCyclicUtil(graph, node, visited, recStack) == True:
                    return print("Graph has a cycle")
        return print("Graph has no cycle")
def concatGraph(graph_1, graph_2):
    graph_out ={}
    #добавить поочереди key из первого графа1
    #проверять есть ли такой key в value,
    #если да то добавить цепочку из графа2
    return graph_1

# Python программа для определения цикла на графике
from collections import defaultdict
def find_circle(graph, path=[]):
    path = path + [start]
    if start == end:
        return path

    if not graph.get(start):
         return None

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path

    if not graph.get(start):
         return None

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
class Veritece():
    def __init__(self, id, num):
        self.id = id
        self.num = num

    def append(self, id):
        return self

    def __str__(self):
        return f'["id" = '+str(self.id)+', "num" = '+str(self.num)+']'

class Graph():
    @classmethod
    def create_from_veriteces(self, vertices):
        return Graph(len(vertices), vertices)

    def __init__(self, quantity, vertices = None):
        #self.graph = defaultdict(list)
        self.graph = vertices
        self.V = quantity

    def __str__(self):
        show_graph = ''
        for key in self.graph:
            show_graph +=str(key)+': ['+str(self.graph[key])+']\n '
        return show_graph

    def addEdge(self, u, v):
        self.graph[u.id].append(v.id)

    def isCyclicUtil(self, v, visited, recStack):
        # Отметить текущий узел как посещенный и добавляет в стек рекурсии
        visited[v] = True
        recStack[v] = True

        # Повтор для всех соседей если любой сосед посещен и в recStack, то график циклический
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # Узел должен быть извлечен из стек рекурсии до завершения функции
        recStack[v] = False
        return False

    # Возвращает true, если график циклический, иначе false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


if __name__ == '__main__':
    # g = Graph(4)
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)

    # if g.isCyclic() == 1:
    #     print("Graph has a cycle")
    # else:
    #     print("Graph has no cycle")

    a = Veritece(0, 1)
    b = Veritece(1, 2)
    c = Veritece(2, 3)
    d = Veritece(3, 4)
    print(a)
    graph = Graph.create_from_veriteces([a, b, c, d])
    graph.addEdge(a, b)
    graph.addEdge(a, c)
    graph.addEdge(b, c)
    graph.addEdge(c, a)
    graph.addEdge(c, d)
    graph.addEdge(d, d)

    print(graph)
# Python программа для определения цикла
# на графике
from collections import defaultdict
from pprint import pprint

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        # Отметить текущий узел как посещенный и
        # добавляет в стек рекурсии

        visited[v] = True
        recStack[v] = True

        # Повтор для всех соседей
        # если любой сосед посещен и в
        # recStack, то график циклический
        print(f' v=' + str(v))
        print(self.graph[v])

        for neighbour in self.graph[v]:
            print(f'neighbour = '+str(neighbour)+' visited[neighbour] = '+str(visited[neighbour])+' recStack[neighbour] = '+str(recStack[neighbour]))
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # Узел должен быть извлечен из
        # стек рекурсии до завершения функции

        recStack[v] = False
        return False

    # Возвращает true, если график циклический, иначе false
    def isCyclic(self):
        print(self.V)
        visited = [False] * self.V
        recStack = [False] * self.V
        print(visited)
        print(recStack)
        for node in range(self.V):
            print(f'visited[' + str(node) + ']=' + str(visited[node]))
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                        return print("Graph has a cycle")
        return print("Graph has no cycle")
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
#g.addEdge(2, 0)
g.addEdge(2, 3)
#g.addEdge(3, 3)
print(g)
if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")



if __name__ == '__main__':
    a = ('A', 1)
    b = ('B', 2)
    c = ('C', 3)
    d = ('D', 4)
    e = ('E', 5)
    f = ('F', 6)

    graph = {a: b,
             b: c,
             c: d}
    print('graph--------------------------')
    pprint(graph)
    print('getGraphKeys---------------------------')
    pprint(getGraphKeys(graph))
    print('isCyclic---------------------------')
    isCyclic(graph)
    print('isOrderUtils---------------------------')
    print(isOrderUtils(graph, a))
    print('isOrder---------------------------')
    isOrder(graph)