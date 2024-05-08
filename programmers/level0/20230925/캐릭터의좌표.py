# 예상 시간복잡도: O(n): len of keyinput

def solution(keyinput, board):
    st = [0,0]
    for dir in keyinput:
        if dir == "left":
            st[0] = max(st[0]-1, -int(board[0]/2))
        elif dir == "right":
            st[0] = min(st[0]+1, int(board[0]/2))
        elif dir == "up":
            st[1] = min(st[1]+1, int(board[1]/2))
        else:
            st[1] = max(st[1]-1, -int(board[1]/2))
    return st


