import TreeNode 

def reconstruct(pre, inord):
  n = len(pre)
  return build(pre, inord, 0, n - 1, 0, n - 1)

# in_l and in_r is start and end of inorder array (inclusive)
# pre_l and pre_r same thing for preorder array(inclusive)
def build(pre, inord, in_l, in_r, pre_l, pre_r):
  if pre_l > pre_r or in_l > in_r:
    return None 


  root = TreeNode.Node(pre[pre_l])

  #NOTE: huge optimization possible here if you use a hash map of
  # values to array indices in pre
  root_idx = inord.index(pre[pre_l])
  left_size = root_idx - in_l

  root.left = build(pre, inord, in_l, root_idx - 1, \
    pre_l + 1, pre_l + left_size)

  root.right = build(pre, inord, root_idx + 1, in_r, \
    pre_l + left_size + 1, pre_r)

  return root 

root = reconstruct(['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I'],\
  ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G'])
res = []
root.print_inord(res)
print res == ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']