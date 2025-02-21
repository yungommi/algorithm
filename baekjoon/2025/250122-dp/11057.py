#예상 시간복잡도 O(n) 

import sys
input = sys.stdin.readline
import math

n = int(input())

l = [[1]*10 for _ in range(n)]

for i in range(1,n):
    for j in range(1,10):
        l[i][j] = l[i-1][j] + l[i][j-1]

ans = sum(l[n-1])
print(int(ans % 10007))