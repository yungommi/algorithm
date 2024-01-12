# 예상 시간복잡도 : O(n)


def solution(n):
    answer = 1
    while True:
        if (6*answer)%n == 0:
            return answer
        else:
            answer += 1




        