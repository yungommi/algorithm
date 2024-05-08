# 예상 시간복잡도: O(N) 

def solution(arr):
    arr.remove(min(arr)) #remove O(N)
    if arr:
        return arr
    else:
        return [-1]