# 예상 시간 복잡도 O(n^2)

def solution(k, tangerine):
    total = len(tangerine)
    d = {}
    for t in tangerine:
        if t in d:
            d[t]+= 1
        else:
            d[t] = 1
    sort_ = sorted(d.items(), key=lambda x:x[1], reverse=True)
    s = len(sort_)
    while True:
        tmp = sort_.pop()
        total -= tmp[1]
        s -= 1
        if total == k:
            return s 
        elif total < k :
            return s+1
        
