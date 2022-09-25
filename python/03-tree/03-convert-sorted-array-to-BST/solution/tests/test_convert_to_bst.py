from  convert_sorted_array_to_bst.convert_to_bst import arr_to_BST

def test_sorted_list_to_BST():
    "happy path"
    list_1 = [4,6,2,1]
    root = arr_to_BST(list_1)
    assert root.value == 4
    assert root.left.value == 2
    assert root.left.left.value == 1
    assert root.right.value == 6
    


