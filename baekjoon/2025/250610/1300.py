#예상시간복잡도 : O(KlogK))
import sys
input = sys.stdin.readline


def function (N,K):
    st,end = 1,N*N 
    while st<=end:
        mid = (st+end)//2 
        tmp = 0 
        for i in range(1,N+1):
            tmp += min(N, mid //i)
        if tmp >= K:
            answer = mid 
            end = mid-1 
        else:
            st = mid+1 
    return (answer)

N = int(input())
K = int(input())
print(function(N,K))