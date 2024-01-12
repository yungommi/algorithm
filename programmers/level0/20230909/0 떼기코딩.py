# 예상 시간복잡도: O(n)

def solution(n_str):
    while True:
        if n_str[0]=='0':
            n_str = n_str[1:]
        else:
            return n_str
        

