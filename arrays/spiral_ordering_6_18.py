# A is an n x n matrix (2-D list)
def spiral(A):
  n = len(A)

  for offset in xrange(n / 2):
    for i in xrange(offset, n - offset - 1):
      print A[offset][i]

    for i in xrange(offset, n - offset - 1):
      print A[i][n - offset - 1]

    for i in xrange(n - offset - 1, offset, -1):
      print A[n - offset - 1][i]

    for i in xrange(n - offset - 1, offset, -1):
      print A[i][offset]

  if n % 2 != 0:
    print A[n / 2][n / 2]

A = [[1,2,3,4],[5,6,7,8], [9,10,11,12], [13,14,15,16]]
spiral(A)
B = [[1,2,3], [4,5,6], [7,8,9]]
spiral(B)