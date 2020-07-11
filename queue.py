#fifo(first in first out)

#using list
q=[]
q.insert(0,"a")
q.insert(0,"b")
q.insert(0,"c")
q.pop()

#using deque
from collections import deque
q=deque()
q.appendleft("a")
q.appendleft("b")
q.appendleft("c")
q.pop()

#using inbuilt queue

# Initializing a queue 
q = Queue(maxsize = 3) 
  
# qsize() give the maxsize  
# of the Queue  
print(q.qsize())  
  
# Adding of element to queue 
q.put('a') 
q.put('b') 
q.put('c') 
  
# Return Boolean for Full  
# Queue  
print("\nFull: ", q.full())  
  
# Removing element from queue 
print("\nElements dequeued from the queue") 
print(q.get()) 
print(q.get()) 
print(q.get()) 
  
# Return Boolean for Empty  
# Queue  
print("\nEmpty: ", q.empty()) 
  
q.put(1) 
print("\nEmpty: ", q.empty())  
print("Full: ", q.full()) 
  
# This would result into Infinite  
# Loop as the Queue is empty.  
# print(q.get()) 

#using python class

class Queue:
  def __init__(self):
    self.que=deque()
  def enqueue(self,val):
    self.que.appendleft(val)
  def dequeue(self):
    self.que.pop()

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        return self.storage.insert(0,new_element)

    def peek(self):
        return self.storage[-1]
        

    def dequeue(self):
        return self.storage.pop()
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()



q=Queue()
q.enqueue("ankit")
print(q.que)
q.enqueue("bansal")
print(q.que)
q.dequeue()  
print(q.que)



