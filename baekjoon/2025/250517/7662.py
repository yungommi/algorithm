#예상시간복잡도 : O(Tklogk)
import sys
input = sys.stdin.readline
import heapq

def function(k):
    minQ = []
    maxQ = []
    alive = [False]*k 
    for i in range(k):
        X,n = input().split()
        n = int(n)
        if X=='I':
            heapq.heappush(minQ, (n,i))
            heapq.heappush(maxQ, (n*-1,i))
            alive[i]=True
        else:
            if n==1 and maxQ:
                alive[heapq.heappop(maxQ)[1]]=False
            elif n==-1 and minQ:
                alive[heapq.heappop(minQ)[1]]=False 
        while minQ and alive[minQ[0][1]]==False:
            heapq.heappop(minQ)
        while maxQ and alive[maxQ[0][1]]==False:
            heapq.heappop(maxQ) 
    if not minQ:
        print("EMPTY")
    else:
        print(-maxQ[0][0], minQ[0][0])


T = int(input())
for i in range(T):
    k = int(input())
    function(k)