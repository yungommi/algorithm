# 예상 시간복잡도: O(n)

def solution(n, numlist):
    answer = []
    for x in numlist:
        if x % n == 0:
            answer.append(x)
    return answer

