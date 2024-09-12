#예상 시간복잡도 O(N^2) 

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tmp = [0 for _ in range(n)]
tmp[0]=1 

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j] and tmp[i] <tmp[j]:
            tmp[i] = tmp[j]
    tmp[i] += 1 

print(max(tmp))