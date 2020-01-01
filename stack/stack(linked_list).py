##  Stack with linked list
##  by seydouxxx (risc@kakao.com || seydoux.tistory.com)
##  2020. 01. 01.
import random

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, node):
        if (self.head is None):
            self.head = node
        else :
            tmp = self.head
            self.head = node
            node.next = tmp
    
    def pop(self):
        if (self.head is None):
            return False
        else :
            print(self.head.data)
            tmp = self.head.next
            self.head = tmp
    
    def peek(self):
        if (self.head is None):
            return False
        else :
            print(self.head.data)        

    def empty(self):
        if (self.head is None):
            return True
        else :
            return False


class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None

#   test case
s = Stack()

for i in range(8):
    s.push(Node(random.randint(1, 100)))

s.peek()

for i in range(10):
    s.pop()