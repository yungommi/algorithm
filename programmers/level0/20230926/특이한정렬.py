# 예상 시간복잡도: O(n)

def solution(numlist, n):
    answer =[]
    for i in numlist:
        answer.append(i - n)
    result = [] 
    for i in sorted(answer, key=lambda x:[abs(x), -x]): 
        result.append(n+i)
    return result


