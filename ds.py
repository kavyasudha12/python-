# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:31:20 2024

@author: gelli
"""

#qstn based on datastructures
#s="{[()]}"
#by using stack we need to implement 
#initially we dont have any element in the stack
#-{-push the element in to the stack
#-[ push the element in to the stack
#-(-push the element in to the stack
#after pushing see the elements that are to be poped out
#s="{}()[]"
#n the above case we push the element as well as we pop the element 

class StackExample:
    def __init__(self):#non paramterized constructor
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def is_empty(self):
        return self.stack==[]
    def pop(self):
        if not  self.is_empty:
                self.stack.pop()
        else:
                print('stack underflow')
    def display(self):
        if not self.is_empty():
         
           for top in range(len(self.stack)-1,-1,-1):
                  print(self.stack[top])
        else:
                  print("stack is empty")
        
    def peek(self):
        if not self.is_empty():
                print('the peek ele:',self.stack[-1])
        else:
                print('the stack is empty')
obj=StackExample()
obj.push(10)
obj.push(20)        
obj.push(30)    
obj.push('varshu')
obj.peek()
obj.display()
