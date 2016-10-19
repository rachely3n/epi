def power(res, idx, a):

  if idx >= len(a):
    res.append([])
    return res

  res = power(res, idx + 1, a)
  temp = []
  for i in xrange(len(res)):
    arr = res[i]
    temp = list(arr)
    temp.append(a[idx])
    res.append(temp)
  
  return res# TODO I think this is not needed 

res = []

power(res, 0, [1,2])

print(res)