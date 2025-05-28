#예상시간복잡도 : O(100000*3))
import sys
input = sys.stdin.readline
from collections import deque

def path(x):
    arr = []
    tmp = x
    for _ in range(dist[x]+1):
        arr.append(tmp)
        tmp = move[tmp]
    arr.reverse()
    print(' '.join(map(str, arr)))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()

'''N,K = map(int, input().split())
moved = [-1]*100001
ans = [100000]*100001
ans[N]=0 
q = deque([N])
while q:
    tmp = q.popleft()
    for x in [tmp-1, tmp+1, tmp*2]:
        if 0<=x<=100000:
            if ans[x]>ans[tmp]+1:
                ans[x]=ans[tmp]+1
                moved[x]=tmp 
                q.append(x)
                #if x==K:
                #    break

a = ans[K]
ll = [K]
tmp = K
while moved[tmp]!=-1:
    ll.append(moved[tmp])
    tmp = moved[tmp]
ll.reverse()
print(a)
print(' '.join(map(str,ll)))'''