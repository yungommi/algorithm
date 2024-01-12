# 예상 시간복잡도: O(n)

def solution(n, k):
    tmp = 0
    answer = []
    while tmp + k <= n:
        tmp += k
        answer.append(tmp)
    return answer

