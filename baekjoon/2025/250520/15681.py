#예상시간복잡도 : O(n)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N,R,Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(N-1):    
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = [0]*(N+1)
visited = [False]*(N+1) 
def function(k):
    visited[k]=True
    if count[k]!=0 :
        return count[k]
    ans = 1
    for x in graph[k]:
        if visited[x] == False:
            ans += function(x)
            visited[x]=True 
    count[k] = ans
    return ans 
function(R)
for i in range(Q):
    k = int(input())
    print(count[k])
