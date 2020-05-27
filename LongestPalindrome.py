"""
cabbacd
abba

"""

import sys
sys.setrecursionlimit(1500)

def isPalindrome(string):
	return string==string[::-1]

def longestPalindrome(string,cache):

	if len(string)==1:
		return string

	if isPalindrome(string):
		return string

	if cache.get(string,0)!=0:
		return cache.get(string,0)

	longString = ""

	for i in range(len(string)):
		currLeft = longestPalindrome(string[0:i], cache)
		currRight = longestPalindrome(string[i+1:], cache)

		if(len(currLeft) > len(longString)):
			longString = currLeft
		if(len(currRight) > len(longString)):
			longString = currRight
			
	cache[string]=longString
	return longString

string = input()

cache = dict()
print( longestPalindrome(string,cache))