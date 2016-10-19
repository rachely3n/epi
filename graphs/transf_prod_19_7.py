from sets import Set
class Vertex:
  def __init__(self, st, dist):
    self.st = st
    self.dist = dist


class Solution:
  def __init__(self, word_dict, s, t):
    self.word_dict = word_dict
    self.s = Vertex(s, 0)
    self.t = Vertex(t, 0) 

  def bfs(self):
    q = [self.s]
    temp_word = ''
    while q:  
      word = q[0]
      if word.st == self.t.st:
        return word.dist 

      n = len(word.st)
      # generate words, unfortunately inefficient
      for i in xrange(n):
        start = end = ''
        if i == 0:
          start = ''
        else: 
          start = word.st[0:i]

        if i + 1 < n:
          end = word.st[i + 1:n]
        else:
          end = ''

        for i in xrange(26):
          #assume all lowercase input
          temp_word = start + chr(ord('a') + i) + end

          # make sure it's in dictionary
          if temp_word in self.word_dict: #let's try this
            # if i'm not mistaken, removal will prevent cycles
            self.word_dict.remove(temp_word)
            q.append(Vertex(temp_word, word.dist + 1))
      

      q = q[1:] # apparently kosher lol

    return -1 

if __name__ == '__main__':
  meep = Solution(Set(['bat', 'cot', 'dog', 'dag', 'dot', 'cat']), 'cat', 'dig')
  print meep.bfs()