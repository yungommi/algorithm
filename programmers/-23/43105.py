# https://school.programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    n = len(triangle)
    tmp = [[0]*n for i in range(n)]
    tmp[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        for j in range(0,i+1):
            if j == 0 :
                tmp[i][j] = tmp[i-1][j] + triangle[i][j]
            else:
                tmp[i][j] = max(tmp[i-1][j] + triangle[i][j], tmp[i-1][j-1]+triangle[i][j])
    
    answer = max(tmp[n-1])
    return answer