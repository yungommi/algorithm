# 예상 시간복잡도: O(n)

def solution(arr, queries):
    for itm in queries:
        x1 = arr[itm[0]]
        x2 = arr[itm[1]]
        arr[itm[0]] = x2
        arr[itm[1]] = x1
    return arr

