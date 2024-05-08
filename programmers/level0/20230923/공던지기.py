# 예상 시간복잡도: O(1)

def solution(numbers, k):
    return numbers[((k-1)*2)%len(numbers)]

