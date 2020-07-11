#lifo (last in first out)
#browser history #ctrl+z  #undo


# implementation of stack using list
# disadvantage : memory reallocation problem
mystack=[]
mystack.append("a")   #addition
mystack.append("b")
mystack.append("c")
mystack.pop()          #remove    #last in will out first


#implementation of stack using deque(double ended queue)
# deque is built upon doubly linkedlist
#solves memory reallocation problem

from collections import deque
mystack=deque()
mystack.append("a")   #addition
mystack.append("b")
mystack.append("c")
mystack.pop()


#implementation of stack using LifoQueue
from queue import LifoQueue
mystack=LifoQueue()
mystack.put("a")   #addition
mystack.put("b")
mystack.put("c")
mystack.get()      #removal

#implementation using python class

class Stack:
  def __init__(self):
    self.stack=[]
  def add(self,dataval):
    self.stack.append(dataval)
  def remove(self):
    self.stack.pop()  
  def peek(self):
    return self.stack[-1] 

# implementation using linkedlist 

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()

stack2=Stack()
stack2.add("a")
stack2.add("a")
print(stack2.peek())
stack2.add("b")   
stack2.add("c") 
print(stack2.peek())
stack2.remove()
print(stack2.peek())
print(stack2.stack)

#without using class
# Stack implementation in python


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))