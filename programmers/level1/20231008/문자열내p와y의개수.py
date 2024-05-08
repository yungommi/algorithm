# 예상 시간복잡도: O(N)


def solution(s):
    pp=0
    yy=0
    for x in s :
        if x.lower() == 'p':
            pp += 1
        elif x.lower()=='y':
            yy+= 1
    if pp+yy == 0 :
        return True
    return pp==yy

