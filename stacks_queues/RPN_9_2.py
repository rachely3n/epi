def RPN(expr):
  operands = []
  operators = ('/', '+', '-', '*') #more if needed

  expr = expr.split(',')

  for val in expr:
    if val in operators:
      # pop
      snd = operands.pop()
      fst = operands.pop()
      # apply the operation
      res = None
      if val == '*':
        operands.append(fst * snd)
      elif val == '+':
        operands.append(fst + snd)
      elif val == "-":
        operands.append(fst - snd)
      else:
        operands.append(fst / snd)
    else:
      operands.append(int(val))

  return operands[-1]

print RPN('3,2,*') == 6
print RPN('3,4,+,2,*,1,+') == 15