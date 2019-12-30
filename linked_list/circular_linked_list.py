##  Circular Linked List
##  by seydouxxx (risc@kakao.com || seydoux.tistory.com)
##  2019. 12. 30.

class LinkedList:
    def __init__(self):
        self.head = None

    #   print all elements by lines
    def show(self):
        if (self.head == None):
            return False
        else :
            point = self.head
            print(point.data)
            while (point.next != self.head):
                point = point.next
                print(point.data)

    #   add element to end of list
    def push(self, node):
        if (self.head is None):
            self.head = node
            node.next = node
        else :
            point = self.head
            while (point.next != self.head):
                point = point.next
            point.next = node
            node.next = self.head
    
    #   delete last element
    def delete(self):
        if (self.head is None):
            return False
        else :
            point = self.head
            while (point.next.next != self.head):
                point = point.next 
            point.next = self.head

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