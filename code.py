class My_Player():
	def __init__(self):
		self.cn=0
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
		print "Old Move:"
		print old_move
		self.cn=0
		next_move = self.minimax(old_move, False, 1000,-1000,board,flag)
		return next_move
	
	def minimax(self,old_move, maximizingPlayer, alpha, beta,board,flag):
		#did u win the game ,if yes it is a leaf node
		hvalue	= self.check_win(board,flag)
		print hvalue
		if(hvalue == 'o'):
			return 10
		elif(hvalue == 'x'):
			return -10
		elif(hvalue == 'd'):
			return 0
		cells = board.find_valid_move_cells(old_move)	
		print "Valid moves:"
		print cells
		for mycell in cells:
			best_move = (-1,-1)
			myblock = [mycell[0]%4, mycell[0]%4]	
			board.board_status[mycell[0]][mycell[1]] = flag
			#did u win the block u placed the flag in
			#if yes change block_status
			winlose = self.check_block(board,flag,myblock)
			print winlose
			if(winlose):
				board.block_status[myblock[0]][myblock[1]] = flag
			if(maximizingPlayer):
				best = -1000;
				val, new_move = self.minimax(mycell, False ,alpha,beta,board,flag)
				board.board_status[mycell[0]][mycell[1]] = '-'
				if best < val:
					best = val
					best_move=mycell
				alpha = self.max(alpha,best)
				if(beta<=alpha):
					break
				return best, best_move
			else:
				best = 1000;
				val, new_move = self.minimax(mycell,True ,alpha,beta,board,flag)
				board.board_status[mycell[0]][mycell[1]] = '-'
				if best > val:
					best = val
					best_move=mycell
				alpha = self.min(alpha,best)
				if(beta<=alpha):
					break
				return best, best_move			

	def check_win(self,board,flag):
		self.cn+=1
		if self.cn>30:
			return True
		whowonorlost = board.find_terminal_state()
		return whowonorlost[1]

	def check_block(self,board,flag,myblock):
		print "ho there"
		bs = board.board_status
		a = 4*myblock[0]
		b = 4*myblock[1]
		#diagonals
		if(bs[a][b] ==  bs[a+1][b+1] == bs[a+2][b+2] ==bs[a+3][b+3] == flag):
			return True
		elif(bs[a][b+3] == bs[a+1][b+2] == bs[a+2][b+1] ==bs[a+3][b] == flag):
			return True
		#columns
		elif(bs[a][b] == bs[a][b+1] == bs[a][b+2] ==bs[a][b+3] == flag):
			return True
		elif(bs[a+1][b] == bs[a+1][b+1] == bs[a+1][b+2] ==bs[a+1][b+3] == flag):
			return True
		elif(bs[a+2][b] == bs[a+2][b+1] == bs[a+2][b+2] ==bs[a+2][b+3] == flag):
			return True
		elif(bs[a+3][b] == bs[a+3][b+1] == bs[a+3][b+2] ==bs[a+3][b+3] == flag):
			return True

		#rows
		elif(bs[a][b] == bs[a+1][b] == bs[a+2][b] ==bs[a+3][b] == flag):
			return True
		elif(bs[a][b+1] == bs[a+1][b+1] == bs[a+2][b+1] ==bs[a+3][b+1] == flag):
			return True
		elif(bs[a][b+2] == bs[a+1][b+2] == bs[a+2][b+2] ==bs[a+3][b+2] == flag):
			return True
		elif(bs[a][b+3] == bs[a+1][b+3] == bs[a+2][b+3] ==bs[a+3][b+3] == flag):
			return True
		return False