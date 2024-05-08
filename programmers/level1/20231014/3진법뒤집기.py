# 예상 시간복잡도: O(logN)

def solution(n):
    return int(three(n),3)

def three(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    return rev_base


