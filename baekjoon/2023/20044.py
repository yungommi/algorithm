# 20044 
# greedy 

from heapq import heappush
from collections import deque 

n = int(input())
item = list(map(int, input().split()))

def function(n,item):
  ans = []
  item.sort()
  item = deque(item)
  for n in range(n):
    heappush(ans, item.pop() + item.popleft())
  return ans[0]

print(function(n,item))

