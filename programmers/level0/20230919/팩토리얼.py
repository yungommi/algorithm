# 예상 시간복잡도: O(k)

def solution(n):
    tmp = 1
    i = 1
    while tmp<n:
        i += 1
        tmp *= i 
        if tmp > n:
            return i-1
    return i



