# 예상 시간복잡도: O(n)

def solution(arr):
    r = len(arr)
    c = len(arr[0])
    if r==c:
        pass
    elif r>c:
        for i in range(r):
            arr[i] = arr[i] + [0]*(r-c)
    else:
        for i in range(r,c):
            arr.append([0]*c)
    return arr
            
    