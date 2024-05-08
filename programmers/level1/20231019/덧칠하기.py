# 예상 시간복잡도: O(N)

def solution(n, m, section):
    count = 1
    tmp = section[0]
    for i in section:
        if tmp + (m - 1) < i:
            tmp = i
            count += 1
    return count