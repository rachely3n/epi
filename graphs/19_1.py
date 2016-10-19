class Node:
	def __init__(self, val):
		self.val = val

def dfs(row, col, board, path, node):
	# assuming an n by n matrix for simplicity
	# otherwise row's boundary is len(board)
		# col is len(board[0])
	if row < 0 or row >= len(board) or col < 0 or col >= len(board)\
	or board[row][col].val == 'black':
		return []

	path.append((row,col))
	if board[row][col] == node:
		return path
	

	#basically mark it discovered/make it invalid	
	board[row][col].val = 'black'
	
	if dfs(row - 1, col, board, path, node) or dfs (row + 1, col, board,\
	path, node) or dfs(row, col - 1, board, path, node) or dfs(row, col + 1, board, path, node) :
		return True 
	else:
		path.pop()
		return False
	
def makeMaze(board):
	rows = len(board)
	cols = len(board[0])
	node_maze = [[None for i in xrange(cols)] for i in xrange(rows)]
	
	for i in xrange(rows):
		for j in xrange(cols):
			
			if board[i][j] == 0:		
				node_maze[i][j] = Node('black')
			else:
				node_maze[i][j] = Node('white')

	return node_maze

if __name__ == "__main__":
	
	board = [[1, 0, 1], [1, 1, 1], [0, 0, 1]]
	node_maze = makeMaze(board)
	path = []
 	dfs(0, 0, node_maze, path,node_maze[2][2])  
 	print path
