def solution(maps):
    answer = 0
    n=(len(maps))
    m=len(maps[1])
    a=0
    b=0
    maps[0][0]= 'x'
    while not(maps[n-1][m-1]=='x'):
        if (a+1<n) and maps[a+1][b]==1 :
            a+=1 
            maps[a][b] = 'x'
        elif (b+1<m) and maps[a][b+1]==1:
            b+=1 
            maps[a][b] = 'x'
        elif (a-1 >= 0) and maps[a-1][b]==1 :
            a-=1 
            maps[a][b] = 'x'
        elif (b-1 >=0) and maps[a][b-1]==1 :
            b-=1 
            maps[a][b] = 'x'
        else:
            return -1
    for i in maps:
        for j in i:
            if j == 'x':
                answer += 1
    return answer

map_ = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
map__ = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(map_))
print(solution(map__))

#내풀이아님
from collections import deque 

def next_step(maps, p):
    nexts = deque()
    n = len(maps) # row size
    m = len(maps[0]) # col size
    # (down, right, up, left)
    for t in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= p[0] + t[0] < n and 0 <= p[1] + t[1] < m:
            if maps[p[0]+t[0]][p[1]+t[1]] == 1:
                nexts.append((p[0]+t[0], p[1]+t[1]))
    return nexts

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])

    end = (n-1, m-1)
    begin = (0, 0)
    maps[0][0] = 0
    begin_item = [begin, 1] # [point, cnt]

    q = deque([begin_item])
    while q:
        current, cnt = q.popleft()

        if current == end:
            return cnt

        nxts = next_step(maps, current)
        for nxt in nxts:
            q.append([nxt, cnt+1])
            maps[nxt[0]][nxt[1]] = 0
    return answer 
