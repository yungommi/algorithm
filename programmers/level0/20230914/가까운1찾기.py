# 예상 시간복잡도: O(n)

def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i]==1:
            return i
    return -1

