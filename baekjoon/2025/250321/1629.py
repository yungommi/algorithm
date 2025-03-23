#예상시간복잡도 : O(N^2) 

import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())
def function(a,b,c):
    if b == 0 :
        return 1 
    if b % 2 == 0 :
        tmp = function(a,b//2,c)
        return (tmp ** 2) % c
    else:
        tmp = function(a,b//2,c)
        tmp = tmp * tmp *  a 
        return tmp % c

print(function(A,B,C))
