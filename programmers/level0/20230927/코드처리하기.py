# 예상 시간복잡도: O(n)

def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if code[i] == '1':
            mode=1 if mode == 0 else 0 
        elif mode ==0 and i%2 == 0 :
            ret += code[i]
        elif mode==1 and i%2 != 0 :
            ret += code[i]
    if ret:
        return ret
    else:
        return "EMPTY"
        
    