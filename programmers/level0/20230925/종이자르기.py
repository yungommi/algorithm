# 예상 시간복잡도: O(1)

def solution(M, N):
    return ( max(M,N)-1 ) + max(M,N) * ( min(M,N)-1 )

