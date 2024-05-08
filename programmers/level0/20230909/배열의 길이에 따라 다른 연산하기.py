# 예상 시간복잡도: O(n)

def solution(arr, n):
    k = len(arr)
    if k%2 == 1:
        for i in range(0,k+1,2):
            arr[i] = arr[i]+n
    else:
        for i in range(1,k,2):
            arr[i] = arr[i]+n
    return arr


