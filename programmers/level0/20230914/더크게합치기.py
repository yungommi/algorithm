# 예상 시간복잡도: O(1)

def solution(a, b):
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    return max(ab,ba)

