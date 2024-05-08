# 예상 시간복잡도: O(n)

def solution(n):
    answer = []
    for x in range(2,n+1):
        if n%x==0 and isprime(x):
            answer.append(x)
    return answer

def isprime(n):
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0 :
            return False
    return True
