# 예상 시간복잡도: O(N)

def solution(n, lost, reserve):
    lost_ = list(set(lost) - set(reserve))
    reserve_ = list(set(reserve)-set(lost))
    for x in reserve_:
        if x-1 in lost_:
            lost_.remove(x-1)   
        elif x+1 in lost_:
            lost_.remove(x+1)
    
    return n - len(lost_)

