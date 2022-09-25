# import pytest
from breadth.breadth_tr import *


# from code_challenges.graph.graph import Graph,Vertex

def test_add_node():
    expected = 'a'
    graph = Graph()
    actual = graph.add_node('a').value
    assert actual == expected

def test_add_edge_exists():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    graph.add_edge(node_a,node_b)
    expected = ['b',0]
    edge = graph.adjacency_list[node_a][0]
    actual = [edge.vertex.value,edge.weight]
    assert actual == expected

# def test_add_edge_does_not_exists():
#     with pytest.raises(KeyError):
#         graph = Graph()
#         node_a = graph.add_node('a')
#         node_b = Vertex('b')
#         graph.add_edge(node_a,node_b)

def test_get_nodes(graph):
    expected = ['a', 'b', 'c', 'd', 'e', 'f']
    nodes = graph.get_nodes()
    actual = []
    for node in nodes:
        actual.append(node.value)
    assert actual == expected

def test_get_neighbors(graph):
    expected = ['c', ['a', 0], ['b', 0], ['e', 0]]
    nodes = graph.get_nodes()
    for node in nodes:
        if node.value == 'c':
            node_c = node
    neighbors = graph.get_neighbors(node_c)
    actual = [node_c.value]
    for edge in neighbors:
        actual += [[edge.vertex.value,edge.weight]]
    assert actual == expected

def test_get_neighbors_with_wieght(graph_weight):
    expected = ['c', ['a', 1], ['b', 5], ['e', 9]]
    nodes = graph_weight.get_nodes()
    for node in nodes:
        if node.value == 'c':
            node_c = node
    neighbors = graph_weight.get_neighbors(node_c)
    actual = [node_c.value]
    for edge in neighbors:
        actual += [[edge.vertex.value,edge.weight]]
    assert actual == expected

def test_get_size(graph):
    expected = 6
    actual = graph.size()
    assert actual == expected

def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    assert not actual

def test_breadth_first_1(graph1):
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    actual = []
    graph,node1 = graph1
    for node in graph.breadth_first(node1):
        actual.append(node.value)
    assert actual == expected

def test_breadth_first_2(graph2):
    expected =  ['a', 'c', 'd', 'b', 'e', 'f']
    actual = []
    graph,node1 = graph2
    for node in graph.breadth_first(node1):
        actual.append(node.value)
    assert actual == expected

def test_breadth_first_3(graph3):
    expected =  ['a', 'Naboo', 'e', 'c', 'Arendelle', 'Metroville']
    actual = []
    graph,node1 = graph3
    for node in graph.breadth_first(node1):
        actual.append(node.value)
    assert actual == expected

def test_depth_first_1(depth_first):
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actual = []
    graph = depth_first
    for node in graph.depth_first():
        actual.append(node.value)
    assert actual == expected

def test_depth_first_2(depth_first2):
    expected =  ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Naboo', 'Narnia']
    actual = []
    graph = depth_first2
    for node in graph.depth_first():
        actual.append(node.value)
    assert actual == expected

def test_depth_first_3():
    graph = Graph()
    actual = graph.depth_first()
    assert not actual


@pytest.fixture
def graph():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c)
    graph.add_edge(node_a,node_d)
    graph.add_edge(node_b,node_c)
    graph.add_edge(node_b,node_f)
    graph.add_edge(node_c,node_e)
    graph.add_edge(node_d ,node_e)
    graph.add_edge(node_e,node_f)
    return graph

@pytest.fixture
def graph_weight():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,1)
    graph.add_edge(node_a,node_d,3)
    graph.add_edge(node_b,node_c,5)
    graph.add_edge(node_b,node_f,7)
    graph.add_edge(node_c,node_e,9)
    graph.add_edge(node_d ,node_e,8)
    graph.add_edge(node_e,node_f,4)
    return graph

@pytest.fixture
def graph1():
    graph = Graph()
    node1 = graph.add_node('Pandora')
    node2 = graph.add_node('Arendelle')
    node3 = graph.add_node('Metroville')
    node4 = graph.add_node('Monstroplolis')
    node5 = graph.add_node('Narnia')
    node6 = graph.add_node('Naboo')
    graph.add_edge(node1, node2)
    graph.add_edge(node2, node3)
    graph.add_edge(node3, node4)
    graph.add_edge(node3, node5)
    graph.add_edge(node3, node6)
    graph.add_edge(node4, node6)
    graph.add_edge(node5, node6)
    return graph,node1

@pytest.fixture
def graph2():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c)
    graph.add_edge(node_a,node_d)
    graph.add_edge(node_b,node_c)
    graph.add_edge(node_b,node_f)
    graph.add_edge(node_c,node_e)
    graph.add_edge(node_d ,node_e)
    graph.add_edge(node_e,node_f)
    return graph,node_a

@pytest.fixture
def graph3():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('Arendelle')
    node_c = graph.add_node('c')
    node_d = graph.add_node('Metroville')
    node_e = graph.add_node('e')
    node_f = graph.add_node('Naboo')
    graph.add_edge(node_a,node_f)
    graph.add_edge(node_b,node_e)
    graph.add_edge(node_c,node_d)
    graph.add_edge(node_e,node_a)
    graph.add_edge(node_f,node_b)
    graph.add_edge(node_a ,node_c)
    graph.add_edge(node_d,node_f)
    return graph,node_a

@pytest.fixture
def depth_first():
    aj_list = Graph()
    a = aj_list.add_node('A')
    b = aj_list.add_node('B')
    c = aj_list.add_node('C')
    d = aj_list.add_node('D')
    e = aj_list.add_node('E')
    f = aj_list.add_node('F')
    g = aj_list.add_node('G')
    h = aj_list.add_node('H')
    aj_list.add_edge(a,b)
    aj_list.add_edge(a,d)
    aj_list.add_edge(b,c)
    aj_list.add_edge(b,d)
    aj_list.add_edge(c,g)
    aj_list.add_edge(d,e)
    aj_list.add_edge(d,h)
    aj_list.add_edge(d,f)
    aj_list.add_edge(h,f)
    return aj_list

@pytest.fixture
def depth_first2():
    graph = Graph()
    node1 = graph.add_node('Pandora')
    node2 = graph.add_node('Arendelle')
    node3 = graph.add_node('Metroville')
    node4 = graph.add_node('Monstroplolis')
    node5 = graph.add_node('Narnia')
    node6 = graph.add_node('Naboo')
    graph.add_edge(node1, node2)
    graph.add_edge(node2, node3)
    graph.add_edge(node3, node4)
    graph.add_edge(node3, node5)
    graph.add_edge(node3, node6)
    graph.add_edge(node4, node6)
    graph.add_edge(node5, node6)
    return graph