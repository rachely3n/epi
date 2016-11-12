# A is a list of ints
# calculate the next permutation
# returns array as next permutation of A
def next_perm(A):
  n = len(A)

  idx = n - 1
  # find decreasing sequence from the tail
  while idx >= 1 and A[idx] < A[idx - 1]:
    idx -= 1


  #find element to swap 
    # if none, there is no possible next permutation
  if idx == 0:
    return []

  swap_idx = idx - 1
  new_spot = -1
  #swap 
  # guaranteed we'll find an element to swap because
  # of termination condition for previous while loop
  while idx < n and A[idx] > A[swap_idx]:
    new_spot = idx
    idx += 1

  A[new_spot], A[swap_idx] = A[swap_idx], A[new_spot]

  # reverse
  l = new_spot  
  r = n - 1
  while l < r: 
    A[l], A[r] = A[r], A[l]
    l += 1
    r -= 1 

  return A 

print next_perm([3,2,1,0]) == []
print next_perm([3,1,2,0]) == [3,2,0,1]
print next_perm([4,2,5,1,3]) == [4,2,5,3,1]