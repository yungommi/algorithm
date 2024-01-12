import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # infinite 10억 

n = int(input()) # 도시의 개수 
m = int(input()) # 버스의 개수 

graph = [[]for i in range(n+1)] # 도시 연결 노드 정보 담는 리스트 
distange = [INF] * (n+1) # 최단거리테이블 무한으로 초기화 

#간선정보 입력받기 
for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c)) 

s,e = map(int,input().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (0,start))
  distance[start] = 0 
  while 1:
    dist, now = heapq.heappop(q) # dist = 0 , now = 1
    if distance[now] < dist:
      continue
    for i in graph[now]: # (2,2), (3,3), (4,1), (5,10)
      cost = dist + i[1]
      if cost < distance[i[0]]: 
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))

dijkstra(s)
print(distance[e])
