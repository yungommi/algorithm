# 예상 시간복잡도: O(nk)

def solution(strlist):
    for i in range(len(strlist)):
        strlist[i] = len(strlist[i])
    return strlist

