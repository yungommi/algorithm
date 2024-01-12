# 예상 시간복잡도: O(n)

def solution(arr):
    for i in range(len(arr)):
        tmp = arr[i]
        if tmp >= 50 and tmp % 2 == 0:
            arr[i] = tmp/2
        elif tmp <50 and tmp % 2 == 1:
            arr[i] = tmp * 2 
    return arr


