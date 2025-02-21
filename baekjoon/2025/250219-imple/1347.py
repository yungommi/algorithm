#예상 시간복잡도 O(n) 

import sys
input = sys.stdin.readline
n = int(input())
str = list(input().rstrip())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x,y,direction= 0,0,1
graph = [[x,y]]

for i in str:
  if i == 'R':
    direction = (direction + 1) % 4
  if i == 'L':
    direction = (direction - 1) % 4
  if i == 'F':
    x = x + dx[direction]
    y = y + dy[direction]
    graph.append([x,y])


n = max(graph)[0] - min(graph)[0] + 1
m = max(graph, key = lambda x:x[1])[1] - min(graph, key = lambda x:x[1])[1] + 1

min_x = min(graph, key = lambda x:x[0])[0] 
min_y = min(graph, key = lambda x:x[1])[1]

for i in graph:
  i[0] = i[0] + abs(min_x)
  i[1] = i[1] + abs(min_y)

# 이중배열 선언 
map =  [[False] *m for _ in range(n)]

for i in graph:
  if map[i[0]][i[1]] == False:
    map[i[0]][i[1]] = '.'

for i in map:
  for j in range(m):
    if i[j] == False:
      i[j] = '#'

for i in map:
  for j in range(len(i)):
    print(i[j],end="")
  print("")