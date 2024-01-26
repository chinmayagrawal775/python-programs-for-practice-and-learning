P1_SYMBOL = "X"; P2_SYMBOL = "O"; a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def check_winner_of_round():
	if  ( (a[0] == a[1] == a[2] == P1_SYMBOL) or 
		  (a[3] == a[4] == a[5] == P1_SYMBOL) or 
		  (a[6] == a[7] == a[8] == P1_SYMBOL) or 
		  (a[0] == a[3] == a[6] == P1_SYMBOL) or 
		  (a[1] == a[4] == a[7] == P1_SYMBOL) or 
		  (a[2] == a[5] == a[8] == P1_SYMBOL) or 
		  (a[0] == a[4] == a[8] == P1_SYMBOL) or 
		  (a[2] == a[4] == a[6] == P1_SYMBOL)
		): return P1_SYMBOL
	elif( (a[0] == a[1] == a[2] == P2_SYMBOL) or 
		  (a[3] == a[4] == a[5] == P2_SYMBOL) or 
		  (a[6] == a[7] == a[8] == P2_SYMBOL) or 
		  (a[0] == a[3] == a[6] == P2_SYMBOL) or 
		  (a[1] == a[4] == a[7] == P2_SYMBOL) or 
		  (a[2] == a[5] == a[8] == P2_SYMBOL) or 
		  (a[0] == a[4] == a[8] == P2_SYMBOL) or 
		  (a[2] == a[4] == a[6] == P2_SYMBOL)
		): return P2_SYMBOL
	else: return "no_winner"

def check_winner_of_round():
	if  ( (a[0] == a[1] == a[2] == P1_SYMBOL) or 
		  (a[3] == a[4] == a[5] == P1_SYMBOL) or 
		  (a[6] == a[7] == a[8] == P1_SYMBOL) or 
		  (a[0] == a[3] == a[6] == P1_SYMBOL) or 
		  (a[1] == a[4] == a[7] == P1_SYMBOL) or 
		  (a[2] == a[5] == a[8] == P1_SYMBOL) or 
		  (a[0] == a[4] == a[8] == P1_SYMBOL) or 
		  (a[2] == a[4] == a[6] == P1_SYMBOL)
		): return P1_SYMBOL
	elif( (a[0] == a[1] == a[2] == P2_SYMBOL) or 
		  (a[3] == a[4] == a[5] == P2_SYMBOL) or 
		  (a[6] == a[7] == a[8] == P2_SYMBOL) or 
		  (a[0] == a[3] == a[6] == P2_SYMBOL) or 
		  (a[1] == a[4] == a[7] == P2_SYMBOL) or 
		  (a[2] == a[5] == a[8] == P2_SYMBOL) or 
		  (a[0] == a[4] == a[8] == P2_SYMBOL) or 
		  (a[2] == a[4] == a[6] == P2_SYMBOL)
		): return P2_SYMBOL
	else: return "no_winner"