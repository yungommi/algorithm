# 예상 시간복잡도: O(k)

def solution(box, n):
    answer = 1
    for x in box:
        answer *= x//n
    return answer

