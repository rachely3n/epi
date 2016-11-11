import sys
def buy_sell_k(A, k):
  n = len(A)
  # sells = [-sys.maxint - 1] * k
  # buys = [-sys.maxint - 1] * k

  data = [-sys.maxint - 1] * (2*k)
  for i in range(2 * k):
    if i % 2 != 0:
      data[i] = 0

  for i in range(n):
    prev = list(data)
    j = 0
    sign = -1
    while j < len(data) and i >= j:
    # for j in range(k):
      if j == 0 :
        diff = sign * A[i]
      else:
        diff = sign * A[i] + prev[j - 1]
        

      data[j] = max(diff, prev[j])
      sign *= -1
      j += 1

  return data[-1]

def buy_sell_k_3(A, k):
  n = len(A)
  sells = [-sys.maxint - 1] * k
  buys = [-sys.maxint - 1] * k


  for i in xrange(n):
    temp = list(buys)
    temp2 = list(sells)
    for j in xrange(k):

      if i >= j: 
        if j == 0:
          buys[j] = max(buys[j],-A[i])
        else:
          buys[j] = max(buys[j], sells[j - 1] - A[i])

    for j in xrange(k):
      if(i + 1) >= 2 * (j + 1): 
        sells[j] = max(sells[j], A[i] + temp[j])
      

  return sells[k - 1]

# i honestly have no idea why this one works....
def buy_sell_k_2(A, k):
  
  n = len(A)
  sells = [0] * n
  buys = [-sys.maxint - 1] * n 
      
  for j in xrange(k):
    for i in xrange(n):
      if i >= j:
        if j == 0:
        # if i > 0:
          buys[i] = max(buys[i - 1], -1 * A[i])
        else: 
          buys[i] = max(buys[i - 1], sells[i - 1] - A[i])

    for i in range(1, n):
      if i + 1 >= 2 * (j + 1):
        sells[i] = max(sells[i - 1], buys[i - 1] + A[i])

  return sells[n - 1]

# why can't we include buys[i][j - 1]?
# o i think it's cause sells will think i did buy and do weird stuff
# https://discuss.leetcode.com/topic/61243/cpp-o-kn-time-and-o-k-space
# i feel like using this for this problem had a lot of blackboxing
# like when there are fewer pairs than transactions
def at_most_k(A, k):
  n = len(A)
  sells = [0] * (k) 
  buys = [-sys.maxint - 1] * k

  buys[0] = -A[0]
  sells[0] = 0
  for i in xrange(n):
    # prev_buys = list(buys)
    # prev_sells = list(sells)
    
    for j in xrange(1,k): 
      #TODO: show buys[j] >= buys[j - 1]
      buys[j] = max(buys[j - 1],buys[j], sells[j - 1] - A[i])
      # buys[j] = max(buys[j], sells[j - 1] - A[i])

      sells[j] = max(sells[j - 1], sells[j], buys[j] + A[i])
      # sells[j] = max(sells[j], prev_buys[j] + A[i])

    #these are necessary since we can't go j - 1 when j is 0 
    buys[0] = max(buys[0], -1*A[i])
    sells[0] = max(sells[0], buys[0] + A[i])
  return sells[k - 1] , buy_sell_k_2(A, k)

print buy_sell_k_3([310, 315, 275, 295, 260, 270, 290, 230, 255, 250], 1)

print buy_sell_k([310, 315, 275, 295, 260, 270, 290, 230, 255, 250], 3)
# print buy_sell_k([2,1], 1)
for i in range(1, 7):
  print at_most_k([310, 315, 275, 295, 260, 270, 290, 230, 255, 250], i)
