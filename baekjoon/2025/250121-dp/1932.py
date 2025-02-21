#예상 시간복잡도 O(n^2) 

import sys
input = sys.stdin.readline

n = int(input())

tri = [[] for i in range(n)]
for _ in range(n):
    inp = list(map(int, input().split()))
    tri[_] = inp 

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            tri[i][j] = tri[i-1][0] + tri[i][j]
        elif j == i:
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
        else:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]

print(max(tri[-1]))