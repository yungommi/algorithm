# 예상 시간복잡도: O(n)

def solution(s1, s2):
    answer = 0
    for x in s1:
        if x in s2:
            answer += 1
    return answer


