# 예상 시간복잡도: O(n)

def solution(a, b):
    x = int(str(a)+str(b))
    y = 2*a*b
    return max(x,y)

