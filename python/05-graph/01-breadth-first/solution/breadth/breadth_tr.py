from collections import deque


class Vertex:

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

class Edge:

    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight

class Queue():

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


class  Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self,value):
        node = Vertex(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self,node1=None,node2=None,weight1=0):
        if node1 not in self.adjacency_list:
            raise KeyError
        elif node2 not in self.adjacency_list:
            raise KeyError
        else:
            edge = Edge(vertex=node2,weight=weight1)
            self.adjacency_list[node1].append(edge)
            edge = Edge(vertex=node1,weight=weight1)
            self.adjacency_list[node2].append(edge)

    def get_nodes(self):
       return self.adjacency_list.keys()

    def get_neighbors(self,node):
        return self.adjacency_list.get(node,[])

    def size(self):
        return len(self.adjacency_list)

    def get_nodes(self):
       return self.adjacency_list.keys()

    def get_neighbors(self,node):
        return self.adjacency_list.get(node,[])

    def size(self):
        return len(self.adjacency_list)

    def breadth_first(self,node):
        queue = Queue()
        queue.enqueue(node)
        visited  = set()
        visited.add(node)
        node_list = []
        def inner_func(queue,visited,node_list):
            for index in range(len(queue)):
                node = queue.dequeue()
                node_list.append(node)
                neighbors = self.get_neighbors(node)
                for edge in neighbors:
                    if edge.vertex not in visited:
                        queue.enqueue(edge.vertex)
                        visited.add(edge.vertex)
            if len(queue) > 0:
                inner_func(queue,visited,node_list)
        inner_func(queue,visited,node_list)
        return node_list

    def depth_first(self):

        nodes = self.get_nodes()
        root = None
        for node in nodes:
            root = node
            break
        result = []
        def inner_func(root,result):
            if root not in result:
                result.append(root)
            neighbors = self.get_neighbors(root)
            for edge in neighbors:
                if edge.vertex not in result:
                    result.append(edge.vertex)
                    inner_func(edge.vertex,result)
        if root:
            inner_func(root,result)
        return result