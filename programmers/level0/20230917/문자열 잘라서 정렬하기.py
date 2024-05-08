# 예상 시간복잡도 : O(n)

def solution(myString):
    tmp = []
    a = myString.split('x')
    for i in a:
        if i != "":
            tmp.append(i)
    tmp.sort()
    return tmp


