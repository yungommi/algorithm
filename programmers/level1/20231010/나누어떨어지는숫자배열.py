# 예상 시간복잡도: O(N)

def solution(arr, divisor):
    answer = []
    for x in arr:
        if x%divisor == 0:
            answer.append(x)
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
    
    