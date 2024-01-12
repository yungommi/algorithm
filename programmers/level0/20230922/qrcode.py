# 예상 시간복잡도: O(n)

def solution(q, r, code):
    answer = ''
    for i in range(r,len(code),q):
        answer += code[i]
    return answer

