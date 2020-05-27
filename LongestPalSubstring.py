"""
cabbacd
abba

"""

import sys
sys.setrecursionlimit(1500)


def isPalindrome(string):
	return string==string[::-1]

def LongestPalindrome(string,i,l):

	if isPalindrome(string[i:l+1]):
		return string[i:l+1]

	if l<0:
		return ""
	if i>len(string):
		return ""

	longPal = ""

	currentPal1 = LongestPalindrome(string, i+1,l)
	currentPal2 = LongestPalindrome(string, i,l-1)

	if len(currentPal1)>len(longPal):
		longPal = currentPal1
	if len(currentPal2)>len(longPal):
		longPal = currentPal2

	return longPal

string = input()

print( LongestPalindrome(string,0,len(string)-1) )