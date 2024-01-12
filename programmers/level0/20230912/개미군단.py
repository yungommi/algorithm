# 예상 시간복잡도: O(1)

def solution(hp):
    answer = 0
    tmp = hp
    answer += tmp // 5
    tmp = tmp % 5
    answer += tmp//3
    answer += tmp % 3
    return answer

