##  Priority Queue
##  by seydouxxx (risc@kakao.com || seydoux.tistory.com)
##  2019. 01. 21.

import random
class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, node):
        print("en : " + str(node.data) + " p : " + str(node.priority))
        if (self.head is None):
            self.head = node
        else :
            i = self.head
            while (i.priority >= node.priority):
                if (i.next is None):
                    i.next = node
                    return
                temp = i
                i = i.next
            if (i is self.head):
                tmp = self.head
                self.head = node
                self.head.next = tmp
            else :
                node.next = i
                temp.next = node
            print(self.head.data)
    
    def dequeue(self):
        if (self.head is not None):
            print("deq : " + str(self.head.data) + " p : " + str(self.head.priority))
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
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


#   test case
q = Queue()

for i in range(8):
    q.enqueue(Node(random.randint(1, 100), random.randint(1, 100)))

q.peek()

for i in range(10):
    q.dequeue()