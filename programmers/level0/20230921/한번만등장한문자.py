# 예상 시간복잡도: O(n)

def solution(s):
    answer = ''
    for i in s:
        if s.count(i)==1:
            answer += i
    return ''.join(sorted(answer))

