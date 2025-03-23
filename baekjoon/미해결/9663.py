#예상시간복잡도 : O(N^2) 

import sys
import copy
input = sys.stdin.readline

N = int(input())

# 초기화
board = [[0] * N for _ in range(N)]
ans = 0

def dfs(row):
    global ans
    if row == N:
        ans += 1
        return

    for col in range(N):
        if not col_used[col] and not diag1[row + col] and not diag2[row - col + N - 1]:
            col_used[col] = diag1[row + col] = diag2[row - col + N - 1] = True
            dfs(row + 1)
            col_used[col] = diag1[row + col] = diag2[row - col + N - 1] = False  # 백트래킹


dfs(0)
print(ans)
