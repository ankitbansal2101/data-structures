#“A Binary Search Tree is sometimes called ordered or sorted binary trees
# it keeps its values in sorted order,
#  so that lookup and other operations can use the principle of binary search”
#An important property of a Binary Search Tree is that 
# the value of a Binary Search Tree node is larger than the value of the offspring of its left child,
#  but smaller than the value of the offspring of its right child.”

class BST:
  def __init__(self,value):
    self.left_child=None
    self.right_child=None
    self.value=value

  #insertion of nodes with some value
   
  def insert_node(self,value):
    if value==self.value:
      return
    elif value<self.value and self.left_child:
      self.left_child.insert_node(value)
    elif value<self.value:
      self.left_child=BST(value)
    elif value>self.value and self.right_child:
      self.right_child.insert_node(value)
    else:
      self.right_child=BST(value)  

  #find a node with some value 

  # We start with the root node as our current node. 
# Is the given value smaller than the current node value? If yes, then we will search for it on the left subtree.
# Is the given value greater than the current node value? If yes, then we will search for it on the right subtree.
# If rules #1 and #2 are both false, we can compare the current node value and the given value if they are equal. 
# If the comparison returns true, then we can say, “Yeah! Our tree has the given value,” 
# otherwise, we say, “Nooo, it hasn’t.”  

  def findnode(self,value):
    if value < self.value and self.left_child:
        return self.left_child.find_node(value)
    if value > self.value and self.right_child:
        return self.right_child.find_node(value)

    return value == self.value  

  #find max value of tree
  def maxtree(self):
    if self.right_child is None:
      return self.data
    
    return self.right_child.maxtree()  

  #find min of tree    
  def mintree(self):
    if self.left_child is None:
      return self.data
    
    return self.left_child.mintree()

  #deletion  
  def delete(self,value):
    if value<self.value:
      if self.left_child:
        




