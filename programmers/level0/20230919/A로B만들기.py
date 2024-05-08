# 예상 시간 복잡도 : O(n)

def solution(before, after):
    tmp1 = list(before)
    tmp2 = list(after)
    tmp1.sort()
    tmp2.sort()
    if tmp1 == tmp2 : 
        return 1
    else:
        return 0
    
 