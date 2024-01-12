# 예상 시간복잡도: O(n)

def solution(n):
    answer = [n]
    x=n
    while x != 1:
        if x%2==0:
            x = x/2
        else:
            x = x*3+1
        answer.append(x)
    return answer

