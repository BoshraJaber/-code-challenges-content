class Node:
    def __init__(self):
        self.val = None
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.next = None
    def insert(self, new_val):
        node = Node()
        node.val = new_val
        node.next = self.head
        self.head = node
        return self.head
    
    def __str__(self):
            string = ''
            current = self.head
            while current:
                string += f'{{{current.val}}}->'
                current = current.next
                if current == None:
                    string += 'NULL'
            return (string)

            
    def deleteNode(self,pointer):
        pointer.val = pointer.next.val
        pointer.next = pointer.next.next


if __name__ == "__main__":
    ll = LL()
    node1= ll.insert(5)
    node2=ll.insert(7)
    node3=ll.insert(2)
    node4=ll.insert(8)
    print(ll.__str__())
    print('==========================')
    ll.deleteNode(node3)
    print(ll.__str__())