#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
l = list(map(int,input().split()))
cul = [0]*(N+1)
for i in range(N):
    cul[i+1] = cul[i] + l[i]

for _ in range(M):
    i,j = map(int,input().split())
    print(cul[j]-cul[i-1])
    