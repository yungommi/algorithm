# 예상 시간복잡도: O(N)

def solution(name, yearning, photo):
    d = {}
    for i in range(len(name)):
        d[name[i]] = yearning[i]
    ans = []
    for col in photo:
        tmp = 0
        for p in col:
            if p in d:
                tmp+=d[p]
        ans.append(tmp)
    return ans

