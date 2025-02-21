# https://www.acmicpc.net/problem/1654

import sys 
input = sys.stdin.readline
n,x = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))

start = 1 
end = max(l)
while start <= end:
    mid = (start+end)//2 
    get = 0
    for i in l:
        get += i // mid
    if get >= x:
        start = mid +1 
    else:
        end = mid-1 
print(end)