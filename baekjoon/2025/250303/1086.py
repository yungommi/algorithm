#예상 시간복잡도 O(M)
# https://www.acmicpc.net/problem/1086 

import sys
input = sys.stdin.readline
from itertools import permutations 
from math import gcd

n = int(input())
s = [0]*n
for _ in range(n):
    s[_] = input().rstrip()

div = int(input())





'''
메모리초과~~
import sys
input = sys.stdin.readline
from itertools import permutations 
from math import gcd

n = int(input())
s = [0]*n
for _ in range(n):
    s[_] = input().rstrip()

div = int(input())
subset = list(permutations(s,n))
total = len(subset)
for i in range(total):
    itm = subset[i]
    tmp = ''.join(itm)
    subset[i] = tmp

suc = 0
for x in subset:
    if int(x)%div == 0:
        suc += 1 
if suc == 0 :
    print("0/1")
else:
    g = gcd(suc, total)
    print(f"{suc//g}/{total//g}")'''
