'''https://www.acmicpc.net/problem/1343'''

import sys
input = sys.stdin.readline

def main(board):
    ans = ''
    nofx = 0 
    for _ in board:
        if _ == 'X':
            nofx += 1
        elif _ == '.':
            if nofx == 0 :
                ans+= '.'
            else:
                q,r = divmod(nofx,4)
                if r == 0 or r == 2:
                    ans += 'AAAA'*q
                    ans += 'BB'*(r//2)
                    nofx = 0 
                    ans += '.'
                else:
                    return -1 
        else: #문자열 끝남 
            q,r = divmod(nofx,4)
            if r == 0 or r == 2:
                ans += 'AAAA'*q
                ans += 'BB'*(r//2)
            else:
                return -1 
    return ans

board = input()
print(main(board))

