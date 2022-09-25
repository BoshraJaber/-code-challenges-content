import pytest
from jordan_trip.jordan_trip import jordan_trip

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

def test_jordan_trip_1(return_graph):
    expected = 197
    actual = jordan_trip(return_graph,['Wadi Musa','Dead sea'])
    assert actual == expected

def test_jordan_trip_2(return_graph):
    expected = 250 
    actual = jordan_trip(return_graph,['Kerak', "Ma'an" ,'Wadi Rum'])
    assert actual == expected

def test_jordan_trip_3(return_graph):
    actual = jordan_trip(return_graph,['Wadi Rum','Dead sea'])
    assert not actual

def test_jordan_trip_4(return_graph):
    actual = jordan_trip(return_graph,['Aqaba','Kerak','Wadi Rum'])
    assert not actual

@pytest.fixture
def return_graph():
    g = Graph()
    node1 = g.add_node('Dead sea')
    node2 = g.add_node('Kerak')
    node3 = g.add_node('Wadi Musa')
    node4 = g.add_node("Ma'an")
    node5 = g.add_node('Aqaba')
    node6 = g.add_node('Wadi Rum') 

    g.add_edge(node1, node2, 82.2)
    g.add_edge(node1, node3, 197)
    g.add_edge(node2, node3, 173)
    g.add_edge(node2, node4, 144)
    g.add_edge(node3, node4, 35.6)
    g.add_edge(node3, node5, 125)
    g.add_edge(node3, node6, 118)
    g.add_edge(node4, node6, 106)
    g.add_edge(node5, node6, 73.9)
    return g