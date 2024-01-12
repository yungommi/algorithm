# 예상 시간복잡도: O(NlogN)

def solution(s):
    l = list(s)
    l.sort(reverse=True)
    return ''.join(l)

