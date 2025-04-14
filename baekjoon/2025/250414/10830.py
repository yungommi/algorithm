#예상시간복잡도 : O(N^3 log B)
import sys
input = sys.stdin.readline

N,B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def matmul(A,B):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += A[i][k]*B[k][j]
            res[i][j] %= 1000
    return res

def power(mat,n):
    if n==1:
        return [[x%1000 for x in row] for row in mat]
    half = power(mat, n//2)
    if n%2==0:
        return matmul(half,half)
    else:
        return matmul(matmul(half,half),mat)
    
ans = power(A,B)
for row in ans:
    print(*row)
