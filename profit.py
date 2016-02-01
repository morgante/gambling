from __future__ import division
import random
import numpy

odds = 0.49
rounds = (100 * 48)

def sim(odds, min, wallet, rounds, goal):
	round = 1
	while (wallet >= min and round <= rounds):
		bet = min

		if (random.random() < odds):
			wallet += bet
		else:
			wallet -= bet

		if (wallet >= goal):
			break

		round += 1

	return wallet

def test(odds, min, wallet, rounds, goal):
	won = 0
	sims = 1000
	returns = []
	for i in range(0,sims):
		result = sim(odds, min, wallet, rounds, goal)

		returns.append(result)

		if (result >= goal):
			won += 1
			# print "In simulation %d, won %d" % (i, result)

	percent = won / sims
	ev = numpy.mean(returns)
	print "Reached $%d in %d of %d sims (%f)" % (goal, won, sims, percent)

	print "Expected return: %d" % (ev)

	return (ev, percent)

# def search():
# 	success = []

# 	for bet in range(10, 1000, 10):
# 		for i in range(1, 50):
# 			wallet = bet * i
# 			goal = wallet + bet

# 			ev = test(odds, bet, wallet, rounds, goal)

# 			print "Expected return on %d: %d" % (wallet, ev)

# 			if (ev > wallet):
# 				success.append((bet, wallet))

# 	print success

def find_bet(wallet, goal):
	bets = []
	for p in range(1, 100, 1):
		bet = wallet * (p/100)
		print("Analyzing bet {bet}".format(bet=bet))
		(ev, percent) = test(odds, bet, wallet, rounds, goal)
		print("For bet of {bet}, ev is {ev} and win percent {percent}".format(bet=bet,ev=ev,percent=percent))
		bets.append((ev, percent))

	print('bets', bets)


def analyze(bet, wallet, goal):
	print("Expected result for betting a {wallet} wallet".format(wallet=wallet))
	print("Bet is {bet} and goal is {goal}".format(bet=bet, goal=goal))

	result = test(odds, bet, wallet, rounds, goal)

	print("EV: {result}".format(result=result))

find_bet(25000, 30000)