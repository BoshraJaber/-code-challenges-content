import pytest

def test_deleteNode(pre):  
    assert pre.__str__() =='{8}->{7}->{5}->NULL'

@pytest.fixture
def pre():
    ll = LL()
    node1=ll.insert(5)
    node2=ll.insert(7)
    node3=ll.insert(2)
    node4=ll.insert(8)
    ll.deleteNode(node3)
    return ll