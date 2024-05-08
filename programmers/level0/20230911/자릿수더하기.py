# 예상 시간복잡도: O(n)

def solution(n):
    answer = 0
    n = str(n)
    for x in n:
        answer += int(x)
    return answer

