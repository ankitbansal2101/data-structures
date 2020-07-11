#A Linked List is a data structure that consists of many mini-data structures called ‘Nodes.’ 
# The Nodes link together to form a list.
# Each node contains 2 attributes
# 1.Its value. This can be anything: integers, characters, strings, objects, and so on.
# 2.A pointer to the next node in the sequence.
#The ‘Head Node’: The head node is simply the first node in the linked list. 

#The ‘Tail Node’: The tail node is the last node in the sequence. Since it’s the last node, it points to null

#creation of a linkedlist

class Node:
  def __init__(self,dataval=None):
    self.dataval=dataval
    self.nextval=None

class LinkedList:

  def __init__(self):
    self.headval=None

  #traversing a linkedlist

  def listprint(self):
    printval=self.headval
    while printval is not None:
      print(printval.dataval)  
      printval=printval.nextval


  #insertion at beginning

  def AtBeginning(self,newdata):
    NewNode=Node(newdata)
    NewNode.nextval=self.headval
    self.headval=NewNode

  
  def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

  # insertion between two nodes
  # insertion at end
  #This involves chaging the pointer of a specific node to point to the new node. 
  # That is possible by passing in both the new node and the existing node after which the new node will be inserted.
  #  So we define an additional class which will change the next pointer of the new node to the next pointer of middle node.
  #  Then assign the new node to next pointer of the middle node.

  def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

  # remove an item from linkedlist

  def RemoveNode(self, Removekey):

        current = self.headval
        if (current == None):
            return

        if (current is not None):
            if (current.data == Removekey):
                self.headval = current.next
                current = None
                return

        while (current is not None):
            if current.data == Removekey:
                break
            prev = current
            current = current.next

        

        prev.next = current.next

        current = None  

  #finding if a particular node exists

  def isnode(self,target):
    curnode=self.headval
    while curnode.nextval is not None:
      if curnode.dataval==target:
        print("exists")
        break
      curnode=curnode.nextval

  #get position of a node

  def get_position(self, position):
    counter = 1
    current = self.head
    if position < 1:
        return None
    while current and counter <= position:
        if counter == position:
            return current
        current = current.next
        counter += 1
    return None    

  # inserting at a particular position
  def insert(self, new_element, position):
    counter = 1
    current = self.headval
    if position > 1:
      while current and counter < position:
        if counter == position - 1:
          new_element.nextval = current.nextval
          current.nextval = new_element
        current = current.nextval
        counter += 1
    elif position == 1:
      new_element.nextval = self.headval
      self.headval = new_element  

  #finding length of linkedlist
  # iterative approach
  def getlength(self):
    current=self.headval 
    counter=0
    while current is not None:
      counter+=1
      current=current.nextval
    return counter  

  #recursive approach
  

    
  
      


 



      

day1=Node("mon")
list1=LinkedList()
list1.headval=day1
day2=Node("tues")
day3=Node("wed")
day1.nextval=day2
day2.nextval=day3

# list1.listprint()
# print("\n")
# list1.AtBeginning("sun")
# list1.listprint()
# print("\n")
# list1.AtEnd("thurs")
# list1.listprint()
# print("\n")
# list1.Inbetween(day2,"ankitday")
# list1.listprint()
# print(day2.dataval)
# print(Node("ankitday").dataval)

print(list1.getlength())





