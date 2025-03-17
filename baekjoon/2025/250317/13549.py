#예상시간복잡도 : O(100000)


import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())

def function(N,K):
    visited = [-1]*100001
    dq= deque()
    dq.append(N)
    visited[N] = 0 
    while dq:
        now = dq.popleft()
        if now==K:
           return visited[K]
        for next in (now*2, now-1, now+1):
            if(0<=next<=100000):
                if visited[next]<0:
                    if next == now*2:
                       visited[next] = visited[now]
                    else:
                       visited[next] = visited[now]+1
                    dq.append(next) 
    return visited[K]

print(function(N,K))
