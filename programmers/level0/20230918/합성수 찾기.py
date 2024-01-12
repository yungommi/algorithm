# 예상 시간 복잡도 : O(n^2)


def solution(n):
    answer = 0
    for x in range(1,n+1):
        for k in range(2,x):
            if x%k ==0:
                answer += 1
                break
    return answer




