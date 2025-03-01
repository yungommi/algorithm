#예상 시간복잡도 O(B)

import sys
input = sys.stdin.readline
import math

A = int(input().rstrip)
B = int(input().rstrip)

ans = 1 
div = 1
for i in range(B):
    ans *= A
    A -= 1

div = 1
for i in range(B):
    div *= (i+1)

print(ans//div)
