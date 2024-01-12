# 예상 시간복잡도: O(N)

def solution(s):
    if (len(s) in [4,6] and s.isdigit()):
        return True
    return False

