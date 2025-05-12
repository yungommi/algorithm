#예상시간복잡도 : O(N)
import sys
input = sys.stdin.readline

def function(M,N,x,y):
    k = x
    while k <= M*N:
        if(k-x)%M==0 and (k-y)%N==0:
            return k 
        k += M 
    return -1 

n = int(input())
for i in range(n):
    a,b,c,d = map(int, input().split())
    print(function(a,b,c,d))
    