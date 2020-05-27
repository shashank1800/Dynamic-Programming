"""
Given a list of items with values and weights, as well as a max weight, 
find the maximum value you can generate from items, where the sum of the 
weights is less than or equal to the max. eg. 

items = {(w:2, v:6), (w:2, v:10), (w:3, v:12)} 
max weight = 5 
knapsack(items, max weight) = 22

w,p,W
10 20 30
60 100 120
50

output:
280

content : www.dynamicprogrammingbook.com


"""

def knapsack(p,w,W,i):

	if i==len(w):
		return 0

	maxProfit = 0

	profitInclude = knapsack(p, w, W-w[i], i+1)
	profitExlude = knapsack(p, w, W, i+1)

	maxProfit = max( profitInclude+p[i], profitExlude)

	return  maxProfit

w = [int(x)for x in input().split()]
p = [int(x)for x in input().split()]

W = int(input())

print( knapsack(p,w,W,0) - p[0] )

