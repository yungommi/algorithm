def solution(m, n, puddles):
    l = [[0]*(m+1) for _ in range(n+1)]
    l[1][1] = 1
    for n in range (1,n+1):
        for m in range(1,m+1):
            if [m,n] not in puddles and [m,n] != [1,1]:
                l[n][m] = l[n-1][m] + l[n][m-1]
    return l[n][m]%1000000007