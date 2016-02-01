import random

def martingale_scheme(odds, wallet, goal, history):
	if len(history) < 1:
		return wallet * 0.1
	return wallet * 0.1

def simulate(odds, wallet, goal, scheme):
	history = []

	while (True):
		bet = scheme(odds, wallet, goal, history)

		if (bet > wallet):
			break

		result = (random.random() < odds)

		row = (wallet, bet, result)
		history.append(row)

		if result:
			wallet += bet
		else:
			wallet -= bet

		if wallet >= goal:
			break

	return wallet

def analyze(odds, wallet, goal):
	result = simulate(odds, wallet, goal, martingale_scheme)

	print('result', result)

analyze(0.49, 100, 110)
