from __future__ import division
import random

odds = 0.49
min = 5
wallet = 5000
rounds = (100 * 24)
goal = wallet + 75

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

won = 0
sims = 1000
for i in range(0,sims):
	result = sim(odds, min, wallet, rounds, goal)

	if (result >= goal):
		won += 1
		print "In simulation %d, won %d" % (i, result)

percent = won / sims
print "Reached $%d in %d of %d sims (%f)" % (goal, won, sims, percent)