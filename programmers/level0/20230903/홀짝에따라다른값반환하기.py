# 예상 시간복잡도: O(1)

def solution(n):
    if n%2==1:
        return int(((n+1)/2)*((n+1)/2))
    else:
        n = n/2
        return int(4*(n*(n+1)*(2*n+1)/6))
    

