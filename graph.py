class Node():
    def __init__(self, id, number, neighborn = None):
        self.id = id
        self.num = number
        self.neighborn = neighborn

    def __str__(self):
        return f'["id" = '+str(self.id)+', "num" = '+str(self.num)+', "neighborn" = '+str(self.neighborn)+']'

class Graph():
#    @classmethodl
    def __init__(self, count, nodes = None):
        self.graph = nodes
        self.V = count

    def __str__(self):
        show_graph = ''
        for key in self.graph:
            show_graph +=str(key)+': ['+str(self.graph[key])+']\n '
        return show_graph

    def create_from_nodes(self, nodes):
        return Graph(len(nodes), nodes)

    def add_nodes(self, left_node, right_node):
        if str(type(left_node)).find('Node') > 0 and str(type(right_node)).find('Node') > 0:
            left_node.neighborn = right_node
            self.graph[left_node.id].append(right_node.id)
        else:
            print('Можно добавлять в граф только узлы с типом "Node" ')

if __name__ == '__main__':
    a01 = Node('A01', 1)
    a02 = Node('A02', 2)
    a03 = Node('A03', 3)
    b04 = Node('B04', 4)
    b05 = Node('B05', 5)
    b06 = Node('B06', 6)
    a08 = Node('A08', 8)
    a09 = Node('A09', 9)
    b11 = Node('B11', 11)
    b12 = Node('B12', 12)
    a18 = Node('A18', 18)

    print(a01)

    g2 = Graph.create_from_nodes([b04, b05, b06, b11, b12])
    g2.add_nodes(b04, b05)
    g2.add_nodes(b05, b06)
    g2.add_nodes(b06, b11)
    g2.add_nodes(b11, b12)

    print(g2)
