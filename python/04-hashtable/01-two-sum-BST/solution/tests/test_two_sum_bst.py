from two_sum_bst.two_sum_bst import Node , BinaryTree ,two_sum_bst

bt = BinaryTree()
bt.root = Node(19)
bt.root.right = Node(10)
bt.root.left = Node(9)


def test_two_sum_bst_True():
    actual = two_sum_bst(bt.root,19)
    expected = True
    assert actual == expected
    
def test_two_sum_bst_False():
    actual = two_sum_bst(bt.root ,10)
    expected = True
    assert actual == expected  
    
def test_two_sum_bst_False_1():
    actual = two_sum_bst(bt.root,5)
    expected = False
    assert actual == expected  

def test_two_sum_bst_False_2():
    BST = BinaryTree()
    actual = two_sum_bst(BST.root,10000)
    expected = False
    assert actual == expected     
    
    
    


