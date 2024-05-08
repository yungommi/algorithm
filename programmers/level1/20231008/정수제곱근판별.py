# 예상 시간복잡도: O(1)

def solution(n):
    rootn = n**0.5
    if rootn.is_integer():
        return (rootn +1)**2
    else:
        return -1 
    
