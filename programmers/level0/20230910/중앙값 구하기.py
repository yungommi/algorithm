# 예상 시간복잡도: O(1)

def solution(array):
    array.sort()
    return array[len(array)//2]

