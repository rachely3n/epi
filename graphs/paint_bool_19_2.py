
class Solution:

  def __init__(self, row, col, board):
    self.row = row
    self.col = col
    self.board = board

  def isFeasible(self, row, col):
    board = self.board
    rows = len(board)
    cols = len(board[0])
    return not(row < 0 or row >= rows or col < 0 or col >= cols or \
      board[row][col] == 0)

  def color(self):
    board = self.board

    row = col = 0
    #assuming valid input
    q = [(self.row, self.col)]
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q: 
      row = q[0][0]
      col = q[0][1]
      q = q[1:] #can you say inefficiency
      for r, c in steps:
        new_row, new_col = row + r, col + c

        if self.isFeasible(new_row, new_col):
          board[new_row][new_col] = 0
          q.append((new_row, new_col))

    print board

  def test(self):
    self.color()


if __name__ == '__main__':
  board = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
  meep = Solution(0, 0, board)
  meep.test()


