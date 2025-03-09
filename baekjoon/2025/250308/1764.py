#예상시간복잡도 : O(N+M)

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
unheard = set()
unseen = set()

for _ in range(N):
    unheard.add(input().rstrip())

for _ in range(M):
    unseen.add(input().rstrip())

unknown = list(unheard&unseen)
unknown.sort()
print(len(unknown))
for x in unknown:
    print(x) 

