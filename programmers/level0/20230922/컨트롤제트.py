# 예상 시간복잡도: O(n)

def solution(s):
    l = s.split()
    n = []
    for x in l:
        if x =='Z':
            n.pop()
        else:
            n.append(x)
    answer = 0
    for i in n:
        answer += int(i)
    return answer

