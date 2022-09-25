import pytest
            
def test_printMiddle_odd_nodes(pre_odd):  
    assert pre_odd.printMiddle() == 7

def test_printMiddle_even_nodes(pre_even):  
    assert pre_even.printMiddle() == 4

@pytest.fixture
def pre_odd():
    ll = LL()
    node1=ll.insert(5)
    node2=ll.insert(7)
    node3=ll.insert(2)
    node4=ll.insert(8)
    ll.__str__()
    ll.printMiddle()
    ll.__str__()
    return ll
@pytest.fixture
def pre_even():
    ll = LL()
    node1=ll.insert(5)
    node2=ll.insert(7)
    node3=ll.insert(4)
    node4=ll.insert(8)
    node5=ll.insert(10)
    ll.__str__()
    ll.printMiddle()
    ll.__str__()
    return ll