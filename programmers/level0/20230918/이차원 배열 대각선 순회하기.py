# 예상 시간 복잡도 : O(n^2)

def solution(board, k):
    answer = 0
    for i in range(0,len(board)):
        for m in range(0,len(board[0])):
            if i + m <= k:
                answer += board[i][m]
    return answer

