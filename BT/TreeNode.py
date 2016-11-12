class Node:
  def __init__(self, val):
    self.val = val 
    self.left = None 
    self.right = None

  def print_inord(self, res):
    
    if self.left:
      self.left.print_inord(res)

    print self.val 
    res.append(self.val)

    if self.right: 
      self.right.print_inord(res)

