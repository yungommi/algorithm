# 예상 시간복잡도: O(n)

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

