##  Singly Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        point = self.head
        while (point is not None):
            print(point.data)
            point = point.next

    def push(self, node):
        if (self.head is None):
            self.head = node
        else:
            point = self.head
            while (point.next is not None):
                point = point.next
            point.next = node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

l = LinkedList()

for i in range(100):
    l.push(Node(i))

l.show()