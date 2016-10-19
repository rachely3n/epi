
class Solution:
  def __init__(self, board):
    self.board = self.makeBoard(board)

  def makeBoard(board):
    rows = len(board)
    cols = len(board[0])
    new_board = [[None for i in xrange(cols)] for i in xrange(rows)]
    
    for i in xrange(rows):
      for j in xrange(cols):
        
        if board[i][j] == 0:    
          new_board[i][j] = 'black'
        else:
          new_board[i][j] = 'white'

    return new_board

  def markIslands(self):
    pass 
  def colorEnclose(self):
    board = self.board
    num_rows = len(self.board)
    num_cols = len(self.board[0])
    canReach = [[False for i in xrange(num_cols)] for i in xrange(numrows)]

    q = []
    for j in xrange(num_cols):
      if board[0][j] == 'white':
        canReach[0][j] == True

      if board[num_rows - 1][j] == 'white':
        canReach[num_rows - 1][j] = True

    for i in xrange(num_rows):
      if board[i][0] == 'white':
        canReach[i][0] = True

      if board[i][num_cols - 1] == 'white':
        canReach[i][num_cols - 1] = True
