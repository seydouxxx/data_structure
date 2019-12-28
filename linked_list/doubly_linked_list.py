##  Doubly Linked List
##  by seydouxxx (risc@kakao.com || seydoux.tistory.com)
##  2019. 12. 28.

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #   print all elements by lines
    def show(self):
        point = self.head
        while (point is not None):
            print(point.data)
            point = point.next

    #   add element to end of list
    def push(self, node):
        if (self.head is None):
            self.head = node
            self.tail = node
        else :
            temp = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.before = temp
    
    #   delete last element
    def delete(self):
        if (self.head is None):
            return False
        else:
            self.tail = self.tail.before
            self.tail.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None

#   test case
l = LinkedList()

for i in range(100):
    l.push(Node(i))

for i in range(10):
    l.delete()

l.show()