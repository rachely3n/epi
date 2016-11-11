def apply_perm(a, p):
  n = len(a)

  # moved = [False] * n 
  completed = 0
  temp = 0
  idx = 0
  while completed < n:
    for i in xrange(n):
      if p[i] != -1:
        temp = i
        idx = i
        break 
    while p[idx] != -1:

      if p[idx] != temp: # trying to find end point of the cycle
        a[p[idx]], a[idx] = a[idx], a[p[idx]]
      temp_idx = p[idx]
      p[idx] = -1

      idx = temp_idx
      completed += 1
      


  return a

sample_4 = ['a','b','c','d']
print apply_perm(sample_4, [2,0,1,3])
print apply_perm(['a','b','c','d'], [3,0,1,2])
print apply_perm(['a','b','c','d'], [3,1,0,2])