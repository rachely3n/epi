# A is a list of ints/floats
# return int/float, max profit from buying and selling once 
def buy_sell(A):
  n = len(A)
  if n <= 1:
    return 0 

  min_val = A[0]
  max_prof = 0
  for price in A:
    max_prof = max(max_prof, price - min_val)
    min_val = min(min_val, price)

  return max_prof 

print buy_sell([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30