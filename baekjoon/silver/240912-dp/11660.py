# 예상시간복잡도 O(n^2)

import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

mat = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    tmp = list(map(int, input().split()))
    mat[i] = [0]+tmp

new = copy.deepcopy(mat)

for i in range(1,n+1):
    for j in range(0,n+1):
       new[i][j] = new[i-1][j] + sum(mat[i][:j+1]) 
    
for i in range(m):
    a,b,c,d = map(int, input().split())
    print(new[c][d]-new[c][b-1]-new[a-1][d]+new[a-1][b-1])

