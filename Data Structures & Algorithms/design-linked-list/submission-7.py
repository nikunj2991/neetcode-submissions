class Node:
    def __init__(self, val: int, next_node: Optional['Node'] = None, prev_node: Optional['Node'] = None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node

class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        result = self.head        
        while index > 0:
            result = result.next_node
            index -= 1
        
        return result.val
            
    def addAtHead(self, val: int) -> None:
        new = Node(val)
        if self.head:
            new.next_node = self.head
            self.head.prev_node = new
            self.head = new
        else:
            self.head = self.tail = new
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        if self.tail:
            self.tail.next_node = new
            new.prev_node = self.tail
            self.tail = new
        else:
            self.head = self.tail = new
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        
        temp = self.head
        while index > 0:
            temp = temp.next_node
            index -= 1
        
        new = Node(val)
        new.next_node = temp
        new.prev_node = temp.prev_node
        temp.prev_node.next_node = new
        temp.prev_node = new
                
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        if self.length == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next_node
            self.head.prev_node = None
        elif index == self.length - 1:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
        else:
            temp = self.head
            while index > 0:
                temp = temp.next_node
                index -= 1
            temp.prev_node.next_node = temp.next_node
            temp.next_node.prev_node = temp.prev_node

        self.length -= 1