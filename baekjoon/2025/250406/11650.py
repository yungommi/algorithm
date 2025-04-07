#예상시간복잡도 : O(NlogN)

import sys
input = sys.stdin.readline

n = int(input())
l = [0]*n
for _ in range(n):
    a,b = map(int,input().split())
    l[_]=(a,b)
l.sort() 
for a,b in l:
    print(a,b)
    