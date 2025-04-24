#예상시간복잡도 : O(N^2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = {i:[] for i in range(1,N+1)}
for i in range(N):
    inp = list(map(int,input().split()))
    node = inp[0] 
    idx = 1
    while inp[idx] != -1 :
        tree[node].append((inp[idx],inp[idx+1]))
        idx += 2 

visited = [-1]*(N+1)
visited[1] = 0

def DFS(node, dist):
    for v, d in tree[node]:
        cal_dist = dist + d
        if visited[v] == -1:
            visited[v] = cal_dist
            DFS(v, cal_dist)
    return
            
DFS(1, 0)
tmp = [0, 0]

for i in range(1, N+1):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i
#print(tmp)

visited = [-1]*(N+1)
visited[tmp[0]] = 0
DFS(tmp[0], 0)

print(max(visited))
