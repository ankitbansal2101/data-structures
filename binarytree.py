# Terminology summary
# Root is the topmost node of the tree
# Edge is the link between two nodes
# Child is a node that has a parent node
# Parent is a node that has an edge to a child node
# Leaf is a node that does not have a child node in the tree
# Height is the length of the longest path to a leaf
# Depth is the length of the path to its root

# “In computer science, a binary tree is a tree data structure in which each node has at the most two children
#  which are referred to as the left child and the right child.” 
# The first thing we need to keep in mind when we implement a binary tree is that it is a collection of nodes. 
# Each node has three attributes: value, left_child, and right_child.

#Here are the rules:

#If the current node doesn’t have a left child, we just create a new node and set it to the current node’s left_child.
#If it does have the left child, we create a new node and put it in the current left child’s place.
# Allocate this left child node to the new node’s left child.
#similar for right node

#there are two options for free traversal
#Depth-First Search (DFS) and Breadth-First Search (BFS)
# DFS is an algorithm for traversing or searching tree data structure. 
# It starts at the root and explores as far as possible along each branch before backtracking.
#DFS explores a path all the way to a leaf before backtracking and exploring another path
#three types of DFS : pre-order,in-order,post-order
#BFS is an algorithm for traversing or searching tree data structure. 
# It starts at the tree root and explores the neighbor nodes first, before moving to the next level neighbors

class BinaryTree:
  def __init__(self,value):
    self.left_child=None
    self.right_child=None
    self.value=value

  #left insertion

  def insert_left(self,value):
    if self.left_child==None:
      NewNode=BinaryTree(value)
      self.left_child=NewNode 
    else:
      NewNode=BinaryTree(value)
      NewNode.left_child=self.left_child
      self.left_child=NewNode

  # right insertion

  def insert_right(self, value):
    if self.right_child == None:
        self.right_child = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.right_child = self.right_child
        self.right_child = new_node    

  #pre-order    #node left right

  def pre_order(self):
    print(self.value)
    if self.left_child:
      self.left_child.pre_order()
    if self.right_child:
      self.right_child.pre_order()  

  #in-order    #left node right

  def in_order(self):
    if self.left_child:
      self.left_child.in_order()
    print(self.value)

    if self.right_child:
        self.right_child.in_order()
  
  #post-order   #left right node

  def post_order(self):
    if self.left_child:
        self.left_child.post_order()

    if self.right_child:
        self.right_child.post_order()

    print(self.value)

  #bfs
  from queue import Queue
  def bfs(self):
    queue = Queue()
    queue.put(self)

    while not queue.empty():
        current_node = queue.get()
        print(current_node.value)

        if current_node.left_child:
            queue.put(current_node.left_child)

        if current_node.right_child:
            queue.put(current_node.right_child)










tree = BinaryTree('a')
print(tree.value) 
print(tree.left_child) 
print(tree.right_child)   
tree.insert_left("b")
print(tree.value) 
print(tree.left_child.value) 
print(tree.right_child)
tree.insert_left("c")
print(tree.value) 
print(tree.left_child.value) 
print(tree.right_child) 
print(tree.left_child.left_child.value) 