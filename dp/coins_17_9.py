def coins(C):
  n = len(C)

  # n x n array of 0's
  A = [[0 for i in xrange(n)] for i in xrange(n)]

  # basically code for filling diagonal by diagonal
    # starting from when i = j to top right diagonal
  for diag in range(n): # n number of diagonals
    offset = diag 
    for step in range(n - offset):
      i = step 
      j = step + offset 

      if i == j:
        A[i][j] = C[i]
      elif j - i == 1:
        A[i][j] = max(C[i], C[j])
      else:
        fst_min = min(A[i + 2][j], A[i + 1][j - 1])
        snd_min = min(A[i][j - 2], A[i + 1][j - 1])
        A[i][j] = max(C[i] + fst_min, C[j] + snd_min)


  return A[0][n - 1] #max profit when game is from C[0 : n]

print coins([1,5,3,7])
print coins([25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10])