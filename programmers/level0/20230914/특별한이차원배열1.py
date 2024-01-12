# 예상 시간복잡도: O(n)

def solution(n):
    answer = [[0]*n for i in range(n)]
    for i in range(n):
        answer[i][i]=1
    return answer

