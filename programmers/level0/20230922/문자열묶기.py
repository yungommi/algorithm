# 예상 시간복잡도: O(n)

def solution(strArr):
    d = {}
    for x in strArr:
        if len(x) in d:
            d[len(x)] += 1
        else:
            d[len(x)]=1
    return max(d.values())

