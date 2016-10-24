def plus_one(a):
  n = len(a)
  for i in xrange(n - 1, -1, -1):
    if a[i] < 9:
      a[i] += 1 #implicit carry 
      return a
    else:
      a[i] = 0 

  # a[0] = 0
  print a
  a.insert(0, 1)
  return a

print plus_one([9,9]) == [1,0,0]
print plus_one([1,9]) == [2,0]
print plus_one([3,8,6]) == [3,8,7]