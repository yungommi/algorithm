# 예상 시간복잡도: O(n^2)

def solution(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j]==arr[j][i]:
                pass
            else:
                return 0
    return 1

