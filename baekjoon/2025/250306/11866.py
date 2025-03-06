#예상시간복잡도 : O(N)

import sys 
input = sys.stdin.readline 
from collections import deque

N,K = map(int,input().split())
q = deque(range(1,N+1))

ans = []
while q:
    q.rotate(-(K-1))
    #deque의 rotate는 뒤에서 앞으로 가져오는것. (-)붙이면 앞에걸 뒤로 갖다붙임 
    popped = q.popleft()
    ans.append(popped)
 

print("<" + ", ".join(map(str,ans))+">")
