class Node:
    def __init__(self,value ):
        self.value  = value
        self.right = None
        self.left = None

def arr_to_BST(arr):
    if not arr:
        return None
  
    # Try to check the middle index
    arr.sort()
    mid = (len(arr)) // 2
     
    # assign the middle element to the root
    root = Node(arr[mid])
     
    # Make the left of the  of root contains all
    # values less than <arr[mid]
    root.left = arr_to_BST(arr[:mid])
    # Make the right of the  of root contains all
    # values bigger than  >arr[mid]
    root.right = arr_to_BST(arr[mid+1:])
    return root


def in_order(root):
    # For printing data it will be in ascending order because inorder visits
    # (left, root ,right) nodes 
    if not root:
        return
    in_order(root.left)   
    print (root.value)
    in_order(root.right)
    
    
if __name__ == "__main__":
    list_1 = [-15,5,10,9]
    root = arr_to_BST(list_1)
    in_order(root)

