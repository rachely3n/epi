# inputs: A is a sorted list
  # note: without sorting, you would need a dict for O(n)
# returns an int of how many unique elements
def delete_dup(A): 
  
  n = len(A)
  if n <= 1:
    return n  

  write_idx = 1
  for i in xrange(1, n):
    if A[i] != A[i - 1]:
      A[write_idx] = A[i]
      write_idx += 1

  return write_idx 

# To prove this, you'd probably do by induction 

print delete_dup([2, 3, 5, 5, 7, 11, 11, 11, 13]) == 6

