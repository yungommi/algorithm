# 예상 시간복잡도: O(n)

def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer

