#예상시간복잡도 : O(N)
import sys
input = sys.stdin.readline
from collections import deque

cog = [0]*4  
for i in range(4):
    cog[i]=input().rstrip() 

def function(k,r):
    dq = deque([(k-1,r)])
    visited = [0]*4 
    while dq:
        tmp,rot = dq.popleft()
        visited[tmp]=1 
        table= cog[tmp]
        left = table[6]
        right = table[2]
        if tmp >=1 and cog[tmp-1][2] != left and visited[tmp-1]==0:
            dq.append((tmp-1, rot*(-1))) 
        if tmp <=2 and cog[tmp+1][6] != right and visited[tmp+1]==0: 
            dq.append((tmp+1, rot*(-1))) 
        if rot == 1:
            cog[tmp]= table[7] + table[:7]
        else: 
            cog[tmp]= table[1:] + table[0]
            
n = int(input())
for i in range(n):
   k, r = map(int,input().split())
   function(k,r) 

ans = 0 
if cog[0][0]=='1':
    ans+= 1
if cog[1][0]=='1':
    ans += 2 
if cog[2][0] =='1':
    ans += 4 
if cog[3][0] == '1':
    ans += 8

print(ans)