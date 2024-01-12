# 예상 시간복잡도: O(n)

def solution(array, n):
    answer = 0
    for x in array:
        if x == n:
            answer += 1
    return answer

