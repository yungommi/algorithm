# 예상 시간 복잡도 : O(n)


def solution(arr, queries):
    for qr in queries:
        for i in range(qr[0], qr[1]+1):
            arr[i]+=1
    return arr

