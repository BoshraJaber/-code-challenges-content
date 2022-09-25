

def two_sum_bst(root, result):
    # create an empty hashmap
    hash_set = set()
   
    def _walk(root1,hash_set1):  
        # base case
        if not root1:
            return False
        
        # add a key -as string- to the hashtable and the value of it is the root value
        hash_set1.add(root1.value)
        # print(hash_set1)
        # traverse the tree       
        if _walk(root1.left,hash_set1):
            return True   
  
        if  _walk(root1.right,hash_set1):
            return True

        subtract_value = abs(result - root1.value)
        print(subtract_value)
        if subtract_value in hash_set:
            return True
        
        return False
    return _walk(root,hash_set)

class Node:
    def __init__(self,value ):
        self.value  = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None 


        