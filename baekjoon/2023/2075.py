# https://www.acmicpc.net/problem/2075

import sys, heapq

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if not heap:
        for a in arr:
            heapq.heappush(heap, a)
    else:
        for a in arr:
            if heap[0] < a:
                heapq.heappush(heap, a)
                heapq.heappop(heap)

print(heap[0])

'''
import sys
n=int(sys.stdin.readline())
 
d=list(map(int, sys.stdin.readline().split())) # 초기값으로 N개 저장
 
for i in range(n-1):
    temp = sorted(list(map(int, sys.stdin.readline().split())) + d, reverse=True)
    d = temp[:n] # 큰 순서대로 N개만 저장
 
print(d[n-1])
'''