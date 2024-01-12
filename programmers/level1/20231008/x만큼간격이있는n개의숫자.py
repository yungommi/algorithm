# 예상 시간복잡도: O(N)

def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x+x*i)
    return answer

