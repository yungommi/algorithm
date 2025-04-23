#예상시간복잡도 : O(K)
import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())    

def function(N,K):
    if K<=N:
        return N-K, 1
    maxlimit = min(100001, 2*K-N)
    way = [0]*(maxlimit+1)
    step = [K]*(maxlimit+1)
    step[N]=0
    way[N]=1
    q = deque([N])
    while q:
        now = q.popleft() 
        #print(now)
        #print(step)
        #print(way)
        for next in [now+1, now-1, now*2]:
            if 0 <= next <= maxlimit:
                if step[next] > step[now]+1:
                    step[next]=step[now]+1 
                    way[next]=way[now]
                    q.append(next)
                elif step[next]==step[now]+1:
                    way[next]+= way[now]
                    #if next not in q:
                    #    q.append(next)
    return step[K], way[K]

a,b = function(N,K)
print(a)
print(b)
