MIN = -1000
MAX = 1000

class My_Player():
	def __init__(self):
		pass
	def min(self,a,b):
		if(a<=b):
			return a
		else:
			return b
	def max(self,a,b):
		if(a>=b):
			return a
		else:
			return b
	def move(self, board, old_move, flag):
		next_move = self.minimax(0,0, False, 1000,-1000,board)
		return next_move
	
	def minimax(self,depth, maximizingPlayer, alpha, beta,board):
		cells = self.find_valid_cells(old_move,board)
		for mycell in cells:
			bestVal = -1000
			best_move = (-1,-1)
			board.board_status[mycell[0]][mycell[1]] = flag
			winlose = self.check_win(board,flag)
			print winlose
			if(winlose):
				board.block_status = flag
			if(maximizingPlayer):
				best = -1000;
				for k in xrange(4):
					val, new_move = self.minimax(depth+1, False ,alpha,beta,board)
					depth = self.max(best,val)
					if best < val:
						best = val
						best_move=mycell
					alpha = self.max(alpha,best)
					if(beta<=alpha):
						break
				return best, best_move
			else:
				best = MAX;
				for k in xrange(4):
					val, new_move = self.minimax(depth+1,True ,alpha,beta,board)
					depth = self.min(best,val)
					if best > val:
						best = val
						best_move=mycell
					alpha = self.min(alpha,best)
					if(beta<=alpha):
						break
				return best, best_move			
		board.board_status[i][j] = '-'
		

	def find_valid_cells(self, old_move,board):
		#returns the valid cells allowed given the last move and the current board state
		allowedcells = []
		allowed_block = [old_move[0]%4, old_move[1]%4]
		#checks if the move is a free move or not based on the rules

		if old_move != (-1,-1) and board.block_status[allowed_block[0]][allowed_block[1]] == '-':
			for i in range(4*allowed_block[0], 4*allowed_block[0]+4):
				for j in range(4*allowed_block[1], 4*allowed_block[1]+4):
					if board.board_status[i][j] == '-':
						allowedcells.append((i,j))
		else:
			for i in range(16):
				for j in range(16):
					if board.board_status[i][j] == '-' and board.block_status[i/4][j/4] == '-':
						allowedcells.append((i,j))
		return allowedcells

	def check_win(self,board,flag):
		
		bs = board.block_status
		answer =  False
		for i in range(4):
			row = bs[i]							#i'th row
			col = [x[i] for x in bs]			#i'th column
			#print row,col
			#checking if i'th row or i'th column has been won or not
			if (row[0] == flag) and (row.count(row[0]) == 4):
				answer = True
			if (col[0] == flag) and (col.count(col[0]) == 4):
				answer = True
		#checking if diagnols have been won or not
		if(bs[0][0] == bs[1][1] == bs[2][2] ==bs[3][3]) and (bs[0][0] == flag):
			answer = True
		if(bs[0][3] == bs[1][2] == bs[2][1] ==bs[3][0]) and (bs[0][3] == flag):
			answer = True
		return answer