# 예상 시간복잡도: O(N)

def solution(s):
    itm = list(map(int,s.split()))
    return str(min(itm))+ " "+str(max(itm))

