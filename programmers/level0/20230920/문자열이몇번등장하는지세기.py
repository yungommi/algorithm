# 예상 시간복잡도: O(n)

def solution(myString, pat):
    l = []
    for i in range(len(myString)):
        tmp=myString[i:].find(pat)
        if tmp>=0 and tmp+i not in l:
            l.append(tmp+i)
    return len(l)