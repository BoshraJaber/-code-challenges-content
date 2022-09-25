def printMiddle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val


if __name__ == "__main__":
    ll = LL()
    node1= ll.insert(5)
    node2=ll.insert(7)
    node3=ll.insert(2)
    node4=ll.insert(8)
    node5= ll.insert(5)
    print(ll.__str__())
    print(ll.printMiddle())
    print('==========================')

