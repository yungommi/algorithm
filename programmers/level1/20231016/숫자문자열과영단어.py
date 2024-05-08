# 예상 시간복잡도: O(N)

def solution(s):
    answer = ''
    num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9' }
    i=0
    len_ = len(s)
    while i < len_:
        if s[i] in '0123456789':
            answer += s[i]
            i+=1 
        elif s[i:i+3] in num:
            answer += num[s[i:i+3]]
            i += 3 
        elif s[i:i+4] in num:
            answer += num[s[i:i+4]]
            i += 4 
        else:
            answer += num[s[i:i+5]]
            i += 5
    return int(answer)

    