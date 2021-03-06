##  Queue with linked list
##  by seydouxxx (risc@kakao.com || seydoux.tistory.com)
##  2019. 12. 30.

import random
class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, node):
        print("enq : " + str(node.data))
        if (self.head is None):
            self.head = node
        else :
            i = self.head
            while (i.next):
                i = i.next
            i.next = node
    
    def dequeue(self):
        if (self.head is not None):
            print("deq : " + str(self.head.data))
            tmp = self.head.next
            self.head = tmp
        else :
            return False
    
    def peek(self):
        if (self.head is not None):
            print("peek : " + str(self.head.data))
        else :
            return False

    def empty():
        if (self.head is None):
            return True
        else :
            return False
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#   test case
q = Queue()

for i in range(8):
    q.enqueue(Node(random.randint(1, 100)))

q.peek()

for i in range(10):
    q.dequeue()