int min = -1000
int max = 1000


class My_Player():
	def __init__(self):
		pass

	def move(self, board, old_move, flag):
		cells = board.best_move(old_move)
		return cells

def minimax(depth, nodeIndex, maximizingPlayer, alpha, beta):
	if(maximizingPlayer):
		int best = MIN;
		for i in xrange(4):
			int val = minimax(depth+1,i+ 2*nodeIndex, false ,alpha,beta)
			depth = max(best,val)
			alpha = max(alpha,best)

			if(beta<=alpha):
				break
		return best
	else:
		int best = MAX;
		for i in xrange(4):
			int val = minimax(depth+1,i+ 2*nodeIndex, true ,alpha,beta)
			depth = min(best,val)
			alpha = min(alpha,best)

			if(beta<=alpha):
				break
		return best



	def best_move(self, old_move):

		bestVal = -1000;
		row=-1;
		col=-1;
		bs = self.block_status

		for i in xrange(4):						#counts the blocks won by x, o and drawn blocks
			for j in xrange(4):
				if (bs[i][j] == '-'):
					bs[i][j] = 'x'
					int moveVal = minimax(board, 0, false, MAX,MIN)
					bs[i][j] == '-'
					if (moveVal > bestVal):
	                    row = i;
	                    col = j;
	                    bestVal = moveVal;
	               