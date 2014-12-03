def is_palindrome(s) :
  l = 0
  r = len(s) - 1
  while l < r :
    while s[l].isalnum() != 1:
      l += 1

    while s[r].isalnum() != 1 :
      r -= 1

    if s[l] != s[r] :
      return False 

    l += 1
    r -= 1

  return True