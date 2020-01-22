##  Stack with array
##  by seydouxxx (risc@kakao.com || seydoux.tistory.com)
##  2020. 01. 01.

import random

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [ None for i in range(self.size) ]
        self.top = 0

    def push(self, data):
        self.stack[self.top] = data
        self.top += 1

    def pop(self):
        if (self.top > 0):
            self.top -= 1
            print(self.stack[self.top])
            self.stack[self.top] = None
        else :
            return

    def peek(self):
        print(self.stack[self.top-1])

    def empty(self):
        for i in range(self.size-1):
            if (self.stack[i] != None):
                return False
        return True

#   test case
s = Stack(10)

for i in range(8):
    s.push(random.randint(1, 100))

s.peek()

for i in range(10):
    s.pop()