# 예상 시간복잡도 : O(n)


def solution(n):
    answer = []
    for i in range(1,n+1):
        if n%i == 0:
            answer.append(i)
    return answer



