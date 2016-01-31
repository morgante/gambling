import random

def ev(odds, bet, profit, wallet):
	if wallet >= profit:
		return wallet
	elif wallet < bet:
		return wallet
	else:
		bet_result = ev(odds, bet, profit, wallet - bet)
		return (odds*(bet_result + bet + bet) + (1-odds)*(bet_result))

print(ev(0.50,1,101,100))

def minmax(odds, bet, profit, wallet):
	print("Simulating flat betting with bet of {bet}", bet=bet)

	