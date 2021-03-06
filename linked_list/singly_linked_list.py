##  Singly Linked List
##  by seydouxxx (risc@kakao.com || seydoux.tistory.com)
##  2019. 12. 26.

class LinkedList:
    def __init__(self):
        self.head = None

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
        else:
            point = self.head
            while (point.next is not None):
                point = point.next
            point.next = node
    
    #   delete last element
    def delete(self):
        if (self.head is None):
            return False
        else:
            point = self.head
            while (point.next.next is not None):
                point = point.next
            point.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#   test case
l = LinkedList()

for i in range(100):
    l.push(Node(i))

for i in range(10):
    l.delete()

l.show()