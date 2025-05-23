#예상시간복잡도 : O(N^2+M)
import sys
input = sys.stdin.readline

N = int(input())
inp = list(map(int, input().split()))
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i]=1 
for i in range(N-1):
    if inp[i]==inp[i+1]:
        dp[i][i+1]=1 
    else:
        dp[i][i+1]=0 
for cnt in range(N-1):
    for i in range(N-2-cnt):
        j = i+2+cnt 
        if inp[i]==inp[j] and dp[i+1][j-1]==1:
            dp[i][j]=1 
        
M = int(input())
for i in range (M):
    a,b = map(int, input().split())
    print(dp[a-1][b-1])


'''시간초과 O(MN)
def ispelindrom(a,b, X):
    if a==b:
        return 1
    else:
        st1 = X[a-1:(a+b-1)//2]
        st2 = X[(a+b)//2:b]
        #print(st1,st2)
        st2.reverse()
        #print(st1,st2)
        for i in range((b-a+1)//2):
            if st1[i]!=st2[i]:
                return 0  
    return 1

N = int(input())
inp = list(map(int, input().split()))
M = int(input())
for i in range (M):
    a,b = map(int, input().split())
    print(ispelindrom(a,b,inp))'''