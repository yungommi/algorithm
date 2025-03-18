#예상시간복잡도 : O(N^2) 

import sys
input = sys.stdin.readline
from collections import deque
     
def function(N):
    if N==1:
        return 0 
    dic = {i:[] for i in range(1,N+1)}
    for _ in range(N-1):
        p,c,w = map(int,input().split())
        dic[p].append((c,w))
        dic[c].append((p,w))
    leaf = []
    for i in range(1,N+1):
        if len(dic[i])==1:
            leaf.append(i)
    ans = 0
    edges = dic[1]
    for ln in leaf:
        visited = [-1]*(N+1)
        dq = deque()
        dq.append(ln)
        visited[ln]= 0
        while dq:
            now = dq.popleft()
            for next,weight in dic[now]:
                if visited[next]==-1:
                    visited[next] = visited[now]+weight
                    dq.append(next)
        ans = max(ans, max(visited))
    return ans

n = int(input())
print(function(n))


'''
O(N)코드 ㅜㅜ 
import sys
from collections import deque

def find_farthest_node(start, graph, n):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([start])
    farthest_node = start
    max_dist = 0
    
    while queue:
        node = queue.popleft()
        for next_node, weight in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + weight
                queue.append(next_node)
                if visited[next_node] > max_dist:
                    max_dist = visited[next_node]
                    farthest_node = next_node
    
    return farthest_node, max_dist

def find_diameter(n):
    if n == 1:
        return 0
    
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(n - 1):
        p, c, w = map(int, input().split())
        graph[p].append((c, w))
        graph[c].append((p, w))
    
    # 1단계: 임의의 노드(1번)에서 가장 먼 노드 찾기
    farthest_node, _ = find_farthest_node(1, graph, n)
    
    # 2단계: 찾은 노드에서 가장 먼 노드까지의 거리가 지름
    _, diameter = find_farthest_node(farthest_node, graph, n)
    
    return diameter

n = int(input())
print(find_diameter(n))
'''