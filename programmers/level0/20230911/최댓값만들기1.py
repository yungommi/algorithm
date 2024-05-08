# 예상 시간복잡도: O(n)

def solution(numbers):
    numbers.sort()
    return numbers[-1]*numbers[-2]

