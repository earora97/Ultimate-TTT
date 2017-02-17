min = -1000
max = 1000

class My_Player():
	def __init__(self):
		pass

	def move(self, board, old_move, flag):
		cells = self.best_move(old_move,board)
		return cells

	def minimax(depth, nodeIndex, maximizingPlayer, alpha, beta):
		if(maximizingPlayer):
			best = MIN;
			for i in xrange(4):
				val = minimax(depth+1,i+ 2*nodeIndex, false ,alpha,beta)
				depth = max(best,val)
				alpha = max(alpha,best)

				if(beta<=alpha):
					break
			return best
		else:
			best = MAX;
			for i in xrange(4):
				val = minimax(depth+1,i+ 2*nodeIndex, true ,alpha,beta)
				depth = min(best,val)
				alpha = min(alpha,best)

				if(beta<=alpha):
					break
			return best

	def best_move(self, old_move,board):
		print "hello"
		my_moves = []
		my_block = [old_move[0]%4, old_move[1]%4]
		bestVal = -1000
		row=-1
		col=-1
		bs = board.block_status
		print bs
		if old_move != (-1,-1) and bs[allowed_block[0]][allowed_block[1]] == '-':
			print "if"
			for i in range(4*my_block[0], 4*my_block[0]+4):
				for j in range(4*my_block[1], 4*my_block[1]+4):
					if bs[i][j] == '-':
						bs[i][j] = flag
						moveVal = minimax(board, 0, false, MAX,MIN)
						bs[i][j] = '-'
						if(moveVal > bestVal):
							row = i
							col = j
							bestVal = moveVal
		else:
			print "else3"
			for i in range(16):
				for j in range(16):
					if bs[i][j] == '-' and bs[i/4][j/4] == '-':
						print "hiii"
						bs[i][j] = flag
						moveVal = minimax(board, 0, false, MAX,MIN)
						bs[i][j] = '-'
						if(moveVal > bestVal):
							row = i
							col = j
							bestVal = moveVal
		print "hi"
		print i,j
		return [(i,j)]
