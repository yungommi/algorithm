# 예상 시간복잡도: O(N)

def solution(n):
    for x in range(2,n):
        if (n-1)%x==0:
            return x
    return 0

