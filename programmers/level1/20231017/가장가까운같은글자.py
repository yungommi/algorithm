# 예상 시간복잡도: O(N)

def solution(s):
    s = s[::-1]
    res = []
    for i in range(len(s)):
        idx = s[i+1:].find(s[i])
        if idx >= 0 :
            res.append(idx+1)
        else:
            res.append(-1)
    return res[::-1]

