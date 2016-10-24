def advance(a):
  n = len(a)
  lower = 0
  upper = a[0] 
  max_idx = -1
  while lower < upper: # maybe n - 1, we'll see

    if upper >= n:
      return True
    max_idx = upper

    for i in range(lower + 1, upper):
      if a[max_idx] + max_idx < i + a[i]:
        max_idx = i 

    lower , upper = max_idx , a[max_idx] + max_idx 

  return False 

def epi(a):

  n = len(a)
  furthest_idx = a[0]
  #invariant is that i should be <= furthest_idx
  for i in xrange(1, n):
    if i <= furthest_idx:
      furthest_idx = max(furthest_idx, i + a[i])

  return furthest_idx >= n - 1


print advance([3,3,1,0,2,0,1])
print advance([2,4,1,1,0,1,0,3])
print advance([3,2,0,0,2,0,1])

print epi([3,3,1,0,2,0,1])
print epi([2,4,1,1,0,1,0,3])
print epi([3,2,0,0,2,0,1])
