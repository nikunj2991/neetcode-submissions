class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next

        while index > 0:
            curr = curr.next
            index -= 1
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        new.prev = self.head
        self.head.next.prev = new
        self.head.next = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        new.prev = self.tail.prev
        new.next = self.tail
        self.tail.prev.next = new
        self.tail.prev = new
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        curr = self.head

        while index > 0:
            curr = curr.next
            index -= 1
        
        new = Node(val)
        new.prev = curr
        new.next = curr.next
        curr.next.prev = new
        curr.next = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.head.next

        while index > 0:
            curr = curr.next
            index -= 1
        
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1

