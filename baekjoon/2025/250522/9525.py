#예상시간복잡도 : O(a*b)
import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip() 
a = len(A)
b = len(B)
dp = [[0]*(b+1) for _ in range(a+1)]
dp_str = [[""]*(b+1) for _ in range(a+1)] 

for i in range(1,a+1):
    for j in range(1,b+1):
        if A[i-1]==B[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            dp_str[i][j]=dp_str[i-1][j-1]+A[i-1]
        else:
            if dp[i-1][j]> dp[i][j-1]:
                dp[i][j]=dp[i-1][j]
                dp_str[i][j]=dp_str[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]
                dp_str[i][j]=dp_str[i][j-1]

print(dp[a][b])
if dp[a][b]!=0 :
    print(dp_str[a][b])
