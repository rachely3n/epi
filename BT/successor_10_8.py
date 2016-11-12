class Node:
  def __init__(self, val):
    self.val = val
    self.parent = None
    self.left = None
    self.right = None   


def BTinordersucc(n):
  if n is None: # note, original solution did not check for this
    return None 

  if n.right:
    n = n.right
    while n.left:
      n = n.left 
    return n 

  else: 

    while n.parent and n == n.parent.right 
      n = n.parent 

    return n.parent # may be None 