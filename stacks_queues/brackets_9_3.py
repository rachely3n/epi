def brackets(string):
  n = len(string)
  if n == 0:
    return True 

  brackets = {"}" : "{", "]" : "[", ")" : "(", ">" : "<"}
  open_bracket = []

  for char in string:
    if char in brackets:
      if not open_bracket:
        return False
      else: 
        if open_bracket[-1] != brackets[char]:
          return False 
        open_bracket.pop()
    else:
      if char == "(" or char == "{" or char == "[" or char == "<":
        open_bracket.append(char)

  return len(open_bracket) == 0


print brackets("()(){")
print brackets("{hello(meow)}")