# 예상 시간복잡도: O(1)

def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

