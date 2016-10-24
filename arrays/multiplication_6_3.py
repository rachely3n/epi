def isneg(n):
  return n < 0

def multiply(a, b):
  n_a = len(a)
  n_b = len(b)
  n_res = n_a + n_b
  res = [0] * (n_res)
  # too many variables? probably 
  res_idx = 0
  temp = 0
  carry = 0 
  neg = False 
  
  #take care of negation
  #when you wish you had ternary operators :(
  if isneg(a[0]) or isneg(b[0]):
    if not (isneg(a[0]) and isneg(b[0])):
      neg = True 
    if isneg(a[0]):
      a[0] *= -1
    if isneg(b[0]):
      b[0] *= -1


  # actual mutiplying
  for i in range(n_a):
    # fill the result at the right place.
    # result should start wherever a starts
    # res_idx = n_a - 1 - i
    for j in range(n_b):
      # actually i implicitly did the i + j because res_idx 
      # was subtracting i and then each time in this inner loop subtract 1
      #
      res_idx = n_res - i - j - 1
      temp = a[n_a - 1 - i] * b[n_b - 1 - j]
      res[res_idx] += temp 
      if res[res_idx] >= 10: 
        temp = res[res_idx]
        carry = temp / 10
        res[res_idx] %= 10 
        res[res_idx - 1] += carry
      # res_idx -= 1
  # get rid of leading 0's 
  write_idx = 0
  last_zero = True
  for i in range(n_res):
    if res[i] == 0 and last_zero:
      write_idx += 1
    else:
      break 

  if neg:
    res[write_idx] *= -1
  return res[write_idx:]

print multiply([1],[2])
print multiply([-9,9], [-9,9])
print multiply([1,6], [1,6])

def epi_multiply(a,b):
  a = a[::-1]
  b = b[::-1]
  n_a = len(a)
  n_b = len(b)
  n_res = n_a + n_b
  res = [0 for i in xrange(n_res)]

  for i in xrange(n_a):
    for j in xrange(n_b):
      res[i + j] += a[i] * b[j]
      res[i + j + 1] += res[i + j] / 10 #never out of range because of 0-indexing 
      res[i + j] %= 10 

  return res[::-1]

print epi_multiply([1],[2])
print epi_multiply([9,9], [9,9])
