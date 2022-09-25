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
    def kth_from_end(self, k):
            if k >= 0:
                if self.head == None:
                    return('The list is empty')
                else:
                    prev = self.head
                    nthNode = self.head
                    dummy = self.head
                    counter = 1
                    current = self.head
                    while dummy.next:
                        dummy = dummy.next
                        if (counter >= k):
                            prev = nthNode
                            nthNode = prev.next
                        counter += 1
                    if prev.next == nthNode.next:
                        self =self.head.next
                        return self
                    prev.next = nthNode.next
                    return self


if __name__ == "__main__":
    ll = LL()
    node1= ll.insert(5)
    node2=ll.insert(7)
    node3=ll.insert(2)
    node4=ll.insert(8)
    print(ll.__str__())
    print('==========================')
    print(ll.kth_from_end(-10))
    print(ll.__str__())
