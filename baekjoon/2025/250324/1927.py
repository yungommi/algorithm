#예상시간복잡도 : O(N log N)

import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
for _ in range(n):
    inp = int(input())
    if inp == 0 :
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,inp)
