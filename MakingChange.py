"""
Given an integer representing a given amount of change, 
write a function to compute the total number of coins 
required to make that amount of change.

getMinChange(1) = 1 (1)
getMinChange(6) = 2 (5 + 1)
getMinChange(49) = 7 (25 + 10 + 10 + 1 + 1 + 1 + 1)

content : www.dynamicprogrammingbook.com

"""

def getMinChange(c,coins,cache):

	if (c<1 or cache[c]!=-1):
		return cache[c]

	minCoin = c+1

	for coin in coins:
		if (c-coin >=0):
			currentMin = getMinChange(c-coin, coins,cache)
			minCoin = min(currentMin, minCoin)

	cache[c] = minCoin+1		
	return cache[c]


coins = [int(x) for x in input("Coins \n").split()]
change = int(input("Change \n"))
cache = [-1] * (change+1)

cache[0] = 0

res = getMinChange(change,coins,cache)
print(res)