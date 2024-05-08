# 예상 시간복잡도: O(n)

def solution(dots):
    dots.sort()
    return (dots[1][1]- dots[0][1])*(dots[2][0]-dots[0][0])

