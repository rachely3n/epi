def min_edit(a, b) :
  # initialize
  # D(i, 0) = i
  # D(0, j) = j
  d = []
  for i in range(len(a) + 1) :
    d.append([])
    d[i].append(i)

  for j in range(len(b) + 1) :
    d[0].append(j)

  for i in range(1, len(a) + 1) : #len(d) gives number of rows
    d.append([])
    for j in range(1, len(b) + 1) :
      if a[i - 1] == b[i - 1] :
        new = d[i - 1][j - 1]
      else :
        # substitution, deletion, insertion for i
        # if we deleted from a, then we have a sequence of operations that 
        # change a[i - 1] to b[j]
        #if we inserted to a, then we have a sequence of operators that
        # change a[i] to j - 1
        new = 1 + min(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1])
      d[i].append(new) #d[i][j] is new

  return d[len(a)][len(b)]

def print_matrix(d) :

  for i in range(len(d)) :
    for j in range(len(d[i])) :
      print d[i][j]


if __name__ == '__main__':
  ans = min_edit('intention', 'execution')
  print ans 
