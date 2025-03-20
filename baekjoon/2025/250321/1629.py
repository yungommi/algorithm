#예상시간복잡도 : O(N^2) 

import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())
A = A% 12
tmp = 1
for _ in range(B):
    tmp = (tmp * A) % C

print(tmp)