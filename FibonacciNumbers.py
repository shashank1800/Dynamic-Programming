"""
Given an integer n, write a function that will return 
the nth Fibonacci number.

fib(0) = 0
fib(1) = 1
fib(5) = 5
fib(10) = 55

content : www.dynamicprogrammingbook.com

"""

import sys
sys.setrecursionlimit(1500)

def findFibonacci(n, cache):

    if(n < 2 or cache[n] != False):
        return cache[n]

    cache[n] = 0                                                                                                                                                              

    fib1 = findFibonacci(n-1, cache)
    fib2 = findFibonacci(n-2, cache)
    
    cache[n] = fib1 + fib2

    return cache[n]

n = int(input())

cache = [False]*(n+1)
cache[0] = 0
cache[1] = 1

res = findFibonacci(n, cache)
print(res)
