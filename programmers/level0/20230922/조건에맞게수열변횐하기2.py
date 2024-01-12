# 예상 시간복잡도: O(n)

def solution(arr):
    answer = 0  
    while True:
        answer += 1
        original = arr[:]
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                arr[i] = arr[i]/2
            elif arr[i]<50 and arr[i]%2==1:
                arr[i] = arr[i]*2 + 1 
        if arr==original:
            break
    return answer-1

