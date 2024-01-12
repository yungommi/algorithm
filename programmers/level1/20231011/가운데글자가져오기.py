# 예상 시간복잡도: O(N)

def solution(s):
    l = len(s)
    if l%2 == 0 :
        return s[l//2-1:l//2+1]
    else:
        return s[l//2]
    
    