#예상시간복잡도 : O(N)
import sys
input = sys.stdin.readline
import math

N, K = map(int,input().split())
coins = [int(input()) for i in range(N)]
n = N-1 

ans = 0 
while K>0:
    ans += (K//coins[n])
    K = K% coins[n]
    n -= 1 
    
print(ans)
