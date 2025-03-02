#예산시간복잡도 O(nlogn)

import sys
input = sys.stdin.readline
N = int(input())
l = [0]*N
for _ in range(N):
    l[_] = int(input())

l.sort()

for x in l:
    print(x)

321
312
231
213
132
213