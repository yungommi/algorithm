#예상시간복잡도 : O(N+M)
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip() 
tmp = 'I'+'OI'*N 
ans = 0
for i in range(0, M-2*N):
    if S[i]=='I' and S[i:i+2*N+1] == tmp:
        ans += 1 
print(ans)
    
