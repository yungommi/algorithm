#예상시간복잡도 : O(N^3)
'''
import sys
input = sys.stdin.readline
from copy import deepcopy 

M,N = map(int,input().split())
x,y,r = map(int,input().split())
room = [0]*N
for i in range(N):
    room[i] = list(map(int,input().split()))

cleaned = [[0]*M for _ in range(N)]
cleaned = deepcopy(room)
rot = [[-1,0],[0,1],[1,0],[0,-1]] 
ans = 0

def function(cleaned, X,Y,R,ans):
    #print(cleaned, X,Y,R,ans)
    if cleaned[X][Y]==0:
        cleaned[X][Y]=1
        ans += 1
        #print('case1')
        #print(ans)
        return cleaned, X,Y,R,ans 

    for _ in range(4):
        R = (R+3)%4 #회전
        nx,ny = X+rot[R][0], Y+rot[R][1] #회전했을때의 전진
        if 0<=nx<N and 0<=ny<M and cleaned[nx][ny]==0: #전진가능하면
            X,Y = nx, ny #전진하고
            cleaned[nx][ny]=1 #청소
            ans += 1
            #print('case2')
            return cleaned, X,Y,R,ans #리턴 / 전진 못해도 회전한채로 리턴 
    #주변 4개 다 청소 되어있음 
    nx,ny = X-rot[R][0], Y-rot[R][1] #후진좌표 찾기
    if 0<=nx<N and 0<=ny<M and room[nx][ny]==0: #후진가능하면
        return cleaned,nx,ny,R,ans #후진
    else: #후진불가능하면 스탑
        #print('case4')
        return 0,X,Y,R,ans 
        
while True:
    cleaned,X,Y,R,ans = function(cleaned, x,y,r,ans) 
    if cleaned == 0 :
        break
print(ans)'''

'''
import sys
input = sys.stdin.readline
from copy import deepcopy 

M,N = map(int,input().split())
x,y,r = map(int,input().split())
room = [0]*N
for i in range(N):
    room[i] = list(map(int,input().split()))

cleaned = [[0]*M for _ in range(N)]
cleaned = deepcopy(room)
rot = [[-1,0],[0,1],[1,0],[0,-1]] 
ans = 0

def function(cleaned, X,Y,R,ans):
    #print(cleaned, X,Y,R,ans)
    if cleaned[X][Y]==0:
        cleaned[X][Y]=1
        ans += 1
        #print('case1')
        #print(ans)
        return cleaned, X,Y,R,ans 
    else:
        for dx,dy in [[-1,0], [1,0], [0,-1], [0,1]]:
            nx,ny = X+dx, Y+dy 
            if 0<=nx<N and 0<=ny<M :
                if cleaned[nx][ny]==0: #주변에 청소안한칸이 있으면 
                    R = (R+3)%4 #회전
                    rx,ry = X+rot[R][0], Y+rot[R][1] #회전했을때의 전진
                    if 0<=rx<N and 0<=ry<M and cleaned[rx][ry]==0: #전진가능하면
                        X,Y = rx, ry #전진하고
                        cleaned[rx][ry]=1 #청소
                        ans += 1
                        #print('case2')
                    return cleaned, X,Y,R,ans #리턴 / 전진 못해도 회전한채로 리턴 
        #주변 4개 다 청소 되어있음 
        rx, ry = X+rot[R][0]*(-1), Y+rot[R][1]*(-1) #후진좌표 찾기
        if 0<=rx<N and 0<=ry<M and room[rx][ry]==0: #후진가능하면
            X,Y = rx,ry 
            #print('case3')
            return cleaned, X,Y,R,ans #후진
        else: #후진불가능하면 스탑
            #print('case4')
            return 0,X,Y,R,ans 
        
while True:
    cleaned,X,Y,R,ans = function(cleaned, x,y,r,ans) 
    if cleaned == 0 :
        break
print(ans)

'''

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
x, y, r = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북동남서
rot = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cleaned = [[0] * M for _ in range(N)]
ans = 0

while True:
    # 현재 위치 청소
    if cleaned[x][y] == 0:
        cleaned[x][y] = 1
        ans += 1

    moved = False
    for _ in range(4):
        r = (r + 3) % 4  # 반시계로 회전
        nx, ny = x + rot[r][0], y + rot[r][1]
        if 0 <= nx < N and 0 <= ny < M and cleaned[nx][ny] == 0 and room[nx][ny] == 0:
            x, y = nx, ny
            moved = True
            break

    if not moved:
        # 4방향 모두 막혔으면 후진
        bx, by = x - rot[r][0], y - rot[r][1]
        if 0 <= bx < N and 0 <= by < M and room[bx][by] == 0:
            x, y = bx, by
        else:
            break

print(ans)