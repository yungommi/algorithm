# 예상 시간복잡도: O(n^2)

def solution(board):
    n = len(board)
    space = [[1]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                for q in range(max(0,i-1),min(n,i+2)):
                    for k in range(max(0,j-1),min(n,j+2)):
                        space[q][k] = 0 
    ans=0
    for item in space:
        ans += sum(item)
    return ans