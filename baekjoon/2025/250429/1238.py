#예상시간복잡도 : O((M+N)logN)

import sys
input = sys.stdin.readline
import math 
import heapq
inf = math.inf

N,M,X = map(int, input().split())

dic = {i:[] for i in range(1,N+1)}
rev_dic = {i:[] for i in range(1,N+1)}
for _ in range(M):
    st,end,t = map(int,input().split())
    dic[st].append((end,t))
    rev_dic[end].append((st,t))

def dijk(start,dic):
    q = []
    distance = [inf]*(N+1)
    heapq.heappush(q,(0,start))
    distance[start]=0 
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue 
        for end, cost in dic[now]:
            if dist+cost < distance[end]:
                distance[end]=dist+cost 
                heapq.heappush(q,(distance[end],end))
    return distance 
go = dijk(X,rev_dic)
back = dijk(X,dic)
res = 0 
for i in range(1,N+1):
    res = max(res, back[i]+go[i])
print(res)
