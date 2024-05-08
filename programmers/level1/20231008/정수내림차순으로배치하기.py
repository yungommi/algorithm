# 예상 시간복잡도: O(N)

def solution(n):
    l = list(str(n))
    l.sort(reverse=True)
    return int(''.join(l))

