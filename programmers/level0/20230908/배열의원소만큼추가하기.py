# 예상 시간복잡도: O(n)

def solution(arr):
    answer = []
    for i in arr:
        answer += [i]*i
    return answer

