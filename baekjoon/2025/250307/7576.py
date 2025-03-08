#예상시간복잡도 : O(N*M)

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for n in range(N):
    for m in range(M):
        if graph[n][m] == 1:
            queue.append((n, m))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

ans = 0
#print(graph)
for row in graph:
    if 0 in row:
        print(-1)
        break
    ans = max(ans, max(row))
else:
    print(ans - 1)


'''
시간초과
import sys 
input = sys.stdin.readline 
import copy

M,N= map(int, input().split())

def function(lists,M,N):
    ans = 0
    new = copy.deepcopy(lists)
    while True: 
        for n in range(1,N+1):
            for m in range(1,M+1):
                if new[n][m]==0:
                    if lists[n-1][m]==1 or lists[n][m-1]==1 or lists[n+1][m]==1 or lists[n][m+1]==1:
                        new[n][m] = 1 
        #print('lists:',lists)
        #print('new:',new)
        if new == lists:
            break 
        else:
            ans += 1 
            lists = copy.deepcopy(new)
    for list in lists:
        if 0 in list:
            return -1
    return ans 

l = [[-1]*(M+2)] *(N+2)
for i in range(1,N+1):
    tmp = [-1]+list(map(int,input().split()))+[-1]
    l[i]=tmp

print(function(l,M,N))'''

