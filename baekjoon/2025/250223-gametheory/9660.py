#예상 시간복잡도 O(1) 

import sys
input = sys.stdin.readline
N=int(input())

if N%7==2 or N%7==0:
    print("CY")
else:
    print("SK")

'''
board = [0]*(N+1)
# -1: SK (1st player)
# +1: CY (2nd player)
board[1] = -1 
board[2] = 1
board[3] = -1
board[4] = -1
board[5] = -1
def function(N):
    if board[N] == 0:
        a,b,c = function(N-1), function(N-3), function(N-4)
        board[N]=max(a,b,c)*-1
    return board[N]

ans = function(N)
if ans==-1:
    print("SK")
else:
    print("CY")
메모리초과
'''